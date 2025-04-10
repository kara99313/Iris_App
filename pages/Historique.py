import streamlit as st
import pandas as pd
import os

st.title("📊 Historique des Prédictions")

history_file = "data/predictions.csv"

if os.path.exists(history_file):
    df = pd.read_csv(history_file)

    st.subheader("🧾 Données enregistrées")
    st.dataframe(df, use_container_width=True)

    # Filtrer par espèce prédite
    selected_species = st.multiselect("Filtrer par espèce prédite :", df["prediction"].unique(), default=df["prediction"].unique())
    filtered_df = df[df["prediction"].isin(selected_species)]

    st.subheader("🔎 Résultats filtrés")
    st.dataframe(filtered_df, use_container_width=True)

    # Télécharger l'historique filtré
    st.download_button("📥 Télécharger l'historique filtré", filtered_df.to_csv(index=False).encode(), "historique_filtré.csv", "text/csv")

else:
    st.warning("Aucune prédiction enregistrée pour le moment.")
