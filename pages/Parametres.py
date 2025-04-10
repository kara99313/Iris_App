import streamlit as st
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Charger les données Iris
iris = load_iris()
X = iris.data
y = iris.target

# Diviser les données en entraînement et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Charger le modèle préexistant
try:
    model = joblib.load("iris_model.pkl")
except FileNotFoundError:
    model = None

st.title("⚙️ Optimisation des Hyperparamètres")
st.markdown("""
    Modifiez les paramètres de votre modèle SVM pour optimiser ses performances.
""")

# Hyperparamètres à modifier
C = st.sidebar.slider("Valeur de C", 0.01, 10.0, 1.0)
kernel = st.sidebar.selectbox("Choisir le kernel", ["linear", "poly", "rbf", "sigmoid"])
degree = st.sidebar.slider("Degré du polynôme (si kernel='poly')", 1, 10, 3)

# Entraînement du modèle avec les nouveaux paramètres
if st.sidebar.button("Entraîner le modèle"):
    try:
        svc = SVC(C=C, kernel=kernel, degree=degree)
        svc.fit(X_train, y_train)
        
        # Prédictions et évaluation
        y_pred = svc.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        st.success("Modèle entraîné avec succès !")
        st.write(f"Précision du modèle : {accuracy:.3f}")
        
        # Enregistrer le modèle (facultatif)
        if st.sidebar.checkbox("Enregistrer le modèle"):
            joblib.dump(svc, "iris_model.pkl")
            st.info("Modèle enregistré avec succès !")
    except Exception as e:
        st.error(f"Erreur lors de l'entraînement du modèle : {e}")

# Afficher le modèle actuel (si chargé)
if model:
    st.write("Modèle actuel :")
    st.write(model)
else:
    st.write("Aucun modèle chargé. Veuillez entraîner un modèle.")
