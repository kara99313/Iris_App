import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Chargement des données Iris
df = sns.load_dataset("iris")

st.title("📈 Analyse des données Iris")
st.markdown("""
    Cette page présente une analyse exploratoire du jeu de données Iris. Vous pourrez visualiser les distributions des caractéristiques et les relations entre elles.
""")

# Afficher les statistiques de base
st.subheader("Statistiques descriptives")
st.write(df.describe())

# Afficher la distribution des caractéristiques
st.subheader("Distribution des caractéristiques")
fig = px.histogram(df, x="sepal_length", color="species", barmode="overlay", title="Distribution de la longueur du sépale")
st.plotly_chart(fig)

fig = px.histogram(df, x="petal_length", color="species", barmode="overlay", title="Distribution de la longueur du pétale")
st.plotly_chart(fig)

# Visualisation des relations entre les variables
st.subheader("Relations entre les variables")
fig = sns.pairplot(df, hue="species")
st.pyplot(fig)
