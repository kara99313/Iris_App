import streamlit as st
import os

# ✅ Cette ligne DOIT être en tout premier
st.set_page_config(page_title="🌸 Prédiction d'Iris", layout="wide")

# Appliquer le style CSS (facultatif mais stylé 😎)
def load_local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Le fichier {file_name} n'a pas été trouvé.")

try:
    load_local_css("assets/style.css")
except Exception as e:
    st.warning(f"Erreur lors du chargement du CSS: {e}")

# 🧼 Masquer les éléments par défaut de Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 👑 Titre principal
st.title("🌸 Application de Prédiction de Fleurs Iris")

# 🧭 Création de la barre de navigation
PAGES = {
    "Accueil": "pages/Accueil.py",
    "Prédiction": "pages/predictions.py",
    "Historique": "pages/Historique.py",
    "Analyse": "pages/Analyse.py",
    "Paramètres": "pages/Parametres.py",
    "À propos": "pages/A_propos.py",
}

# Navigation par menu radio
page = st.sidebar.radio("Naviguer", list(PAGES.keys()))

# Vérification de l'existence du fichier et exécution sécurisée
if os.path.exists(PAGES[page]):
    with open(PAGES[page], encoding="utf-8") as f:
        code = f.read()
        exec(code)
else:
    st.error(f"Le fichier {PAGES[page]} n'existe pas.")
    st.info("Vérifiez le chemin du fichier ou créez-le.")