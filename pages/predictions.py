import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import os
from datetime import datetime

st.title("🔍 Prédiction de l'espèce d'une fleur d'Iris")
model = joblib.load("iris_model.pkl")
species = ['Setosa', 'Versicolor', 'Virginica']

st.sidebar.header("🧪 Paramètres de la fleur")
sepal_length = st.sidebar.slider("Longueur du sépale (cm)", 4.0, 8.0, 5.1)
sepal_width = st.sidebar.slider("Largeur du sépale (cm)", 2.0, 4.5, 3.5)
petal_length = st.sidebar.slider("Longueur du pétale (cm)", 1.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Largeur du pétale (cm)", 0.1, 2.5, 0.2)

if st.sidebar.button("Prédire"):
    input_df = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                             columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
    prediction = model.predict(input_df)
    probabilities = model.predict_proba(input_df)[0]
    predicted_species = species[prediction[0]]

    st.success(f"🌿 Résultat : **{predicted_species}**")

    # Graphique interactif
    fig = go.Figure([go.Bar(x=species, y=probabilities, marker_color=['#f94144','#f3722c','#90be6d'])])
    fig.update_layout(title="Probabilités de chaque espèce", yaxis_title="Probabilité")
    st.plotly_chart(fig)

    # Enregistrement
    history_file = "data/predictions.csv"
    input_df["prediction"] = predicted_species
    input_df["probability_setosa"] = probabilities[0]
    input_df["probability_versicolor"] = probabilities[1]
    input_df["probability_virginica"] = probabilities[2]
    input_df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Créer le dossier 'data' s'il n'existe pas
    os.makedirs("data", exist_ok=True)

    if os.path.exists(history_file):
        history_df = pd.read_csv(history_file)
        history_df = pd.concat([history_df, input_df], ignore_index=True)
        history_df.to_csv(history_file, index=False)
    else:
        input_df.to_csv(history_file, index=False)

    st.success("✅ Prédiction enregistrée dans le fichier `data/predictions.csv`")

    # Téléchargement CSV
    st.download_button("📥 Télécharger la prédiction", input_df.to_csv(index=False).encode(), "prediction.csv", "text/csv")
