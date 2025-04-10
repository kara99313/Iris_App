import streamlit as st
import base64
from datetime import datetime
import random

# --- ARRIÈRE-PLAN PERSONNALISÉ ---
st.markdown(
    """
    <style>
    body {
        background-image: url('iris_fleur_accueil.png');
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True
)

# --- PAGE D'ACCUEIL ---
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🌸 Bienvenue dans l'application Iris</h1>
    <p style='text-align: center; font-size:18px;'>Prédisez l'espèce d'une fleur avec l'intelligence artificielle 🤖</p>
""", unsafe_allow_html=True)

# --- ANIMATION DU TITRE ---
st.markdown("""
    <style>
    h1 {
        animation: shine 2s infinite;
    }
    @keyframes shine {
        0% { color: #4CAF50; }
        50% { color: #FF6347; }
        100% { color: #4CAF50; }
    }
    </style>
""", unsafe_allow_html=True)

# --- IMAGE ILLUSTRATIVE ---
st.image("assets/iris_fleur.png", caption="Une illustration botanique des fleurs d'Iris 🌸", use_column_width=True)

# --- DATE & HEURE ---
now = datetime.now().strftime("%A %d %B %Y, %H:%M:%S")
st.markdown(f"<p style='text-align:right; color:gray;'>🕒 {now}</p>", unsafe_allow_html=True)

# --- COMPTEUR DE PRÉDICTIONS ---
if 'prediction_count' not in st.session_state:
    st.session_state.prediction_count = 0
st.session_state.prediction_count += 1
st.markdown(f"<p style='text-align:center; font-size:18px;'>🔢 Nombre de prédictions effectuées : {st.session_state.prediction_count}</p>", unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown("---")
st.subheader("📁 Accès rapide")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔍 Faire une prédiction"):
        st.switch_page("pages/predictions.py")

with col2:
    if st.button("📊 Analyse des données"):
        st.switch_page("pages/Analyse.py")

with col3:
    if st.button("🕘 Historique des prédictions"):
        st.switch_page("pages/Historique.py")

# --- GUIDE D'UTILISATION ---
st.markdown("---")
st.markdown("<h3>🧭 Comment utiliser l'application ?</h3>", unsafe_allow_html=True)
with st.expander("📘 Guide étape par étape"):
    st.markdown("""
    1. Rendez-vous dans l'onglet **"Faire une prédiction"**.
    2. Ajustez les curseurs selon les caractéristiques de la fleur.
    3. Cliquez sur **Prédire** pour découvrir l'espèce.
    4. Allez dans **Historique** pour revoir toutes vos prédictions.
    5. Consultez **Analyse** pour explorer les statistiques globales.
    """)

# --- CITATION INSPIRANTE ---
citations = [
    "\"L'intelligence artificielle ne remplacera pas les humains, mais ceux qui l'utilisent remplaceront ceux qui ne le font pas.\"",
    "\"La nature est la meilleure des ingénieures.\"",
    "\"Science is magic that works.\" - Kurt Vonnegut",
    "\"Ce que nous savons, c’est une goutte d’eau ; ce que nous ignorons est un océan.\" - Isaac Newton",
    "\"L'observation fine d'une fleur est une porte d'entrée vers les mystères du vivant.\"",
    "\"Les fleurs sont les sourires de la nature.\""
]
st.info(random.choice(citations))

# --- INFOS SUPPLÉMENTAIRES ---
st.markdown("---")
with st.expander("ℹ️ À propos de l'application"):
    st.markdown("""
    Cette application a été développée par **Idriss** dans le cadre d'un projet Data Science. 
    Elle repose sur un modèle de classification supervisée entraîné à partir du célèbre jeu de données **Iris**.

    **Technologies utilisées :**
    - Python 🐍
    - Streamlit 🖥️
    - Scikit-learn 🤖
    - Plotly 📊
    - Pandas 🐼

    🎯 Objectif : Montrer de manière ludique et interactive l'utilisation de l'intelligence artificielle dans un problème réel de classification !

    📚 Ce projet met également en avant la beauté et la diversité des fleurs Iris, avec une touche artistique pour stimuler l'engagement visuel.

    🔗 [Voir le code sur GitHub](https://github.com/ton_profil/iris-app) *(à personnaliser)*

    🧠 **Conseil IA du jour** : Saviez-vous que l'IA peut aider à diagnostiquer des maladies à partir d'images médicales ?
    """)

# --- LIEN VERS GITHUB ET PROFIL ---
st.markdown("---")
st.markdown("""
    🔗 **GitHub du projet** : [Voir le projet sur GitHub](https://github.com/ton_profil/iris-app)  
    🧑‍💻 **Profil LinkedIn de l'auteur** : [Connectez-vous avec Idriss sur LinkedIn](https://www.linkedin.com/in/ton_profil/)
""")
