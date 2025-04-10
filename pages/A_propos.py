import streamlit as st

# Titre de la page "À propos"
st.title("ℹ️ À propos de cette application")

# Introduction sur le projet
st.markdown("""
Cette application a été créée pour démontrer l'utilisation des techniques de machine learning appliquées à un problème classique de classification des fleurs d'Iris. L'objectif principal de ce projet est d'offrir une interface interactive qui permet aux utilisateurs de faire des prédictions à l'aide de modèles déjà entraînés.

### Contexte du projet
Le jeu de données Iris est un ensemble de données bien connu dans le domaine de la Data Science, qui consiste à prédire l'espèce de fleurs d'Iris (Setosa, Versicolor, Virginica) en fonction de plusieurs caractéristiques : la longueur et la largeur des sépales et des pétales. Ce jeu de données a été utilisé pour tester l'efficacité de plusieurs algorithmes de classification, notamment les modèles linéaires et non linéaires.

---

### 🚀 Pourquoi ce projet ?
Le projet vise à démontrer l'efficacité des modèles de machine learning pour résoudre des problèmes réels, tout en offrant une interface simple et intuitive. L'application permet à tout utilisateur, même débutant, de réaliser des prédictions facilement et de comprendre comment fonctionnent les modèles de classification.

En utilisant **Streamlit**, l’application est conçue pour être interactive, afin d'offrir une expérience utilisateur fluide et pédagogique.

---

### 🛠️ Technologies et outils utilisés :
Voici les principales technologies et bibliothèques utilisées dans ce projet :

- **Python** : Langage de programmation utilisé pour le développement de l'application.
- **Streamlit** : Framework pour la création d'interfaces web interactives et conviviales.
- **Scikit-learn** : Bibliothèque de machine learning pour entraîner et évaluer des modèles de classification.
- **Plotly** : Outil pour créer des visualisations interactives et dynamiques des résultats.
- **Pandas** : Bibliothèque pour la manipulation et le nettoyage des données tabulaires.

---

### 🌱 Objectifs du projet :
- **Comprendre et appliquer** des techniques de classification supervisée avec des algorithmes de machine learning.
- **Simplifier l'accès** à l'intelligence artificielle pour les débutants grâce à une interface intuitive.
- **Illustrer les principes** du machine learning à travers un exemple concret et accessible à tous.
- **Offrir un environnement interactif** où l'utilisateur peut faire des prédictions et visualiser les résultats.

---

### 📚 À propos du jeu de données Iris :
Le jeu de données Iris a été collecté par **Anderson** en 1935 et est un standard dans l'apprentissage automatique. Il contient 150 échantillons de trois espèces de fleurs d'Iris, avec quatre caractéristiques mesurées pour chaque échantillon : 
1. La longueur du sépale.
2. La largeur du sépale.
3. La longueur du pétale.
4. La largeur du pétale.

Les modèles utilisés dans cette application permettent de prédire l'espèce de la fleur en fonction de ces quatre caractéristiques.

---

### 👨‍💻 À propos de l'auteur :
**Idriss** est un passionné de Data Science, Machine Learning et Visualisation des données. Son objectif est de rendre ces technologies accessibles à un large public, en particulier aux débutants. Son travail consiste à simplifier les concepts complexes et à les rendre facilement compréhensibles.

- **Nom** : Idriss
- **Contact** : [LinkedIn](https://www.linkedin.com/in/tonprofil) | [GitHub](https://github.com/tonprofil) | **Email** : idriss@example.com
- **Passions** : Data Science, Intelligence Artificielle, Visualisation des données, et Education.

---

### 💬 Contactez-moi :
Si vous avez des questions, des suggestions, ou si vous souhaitez discuter de ce projet ou d’autres initiatives en Data Science, n'hésitez pas à me contacter !

- **Email** : idriss@example.com
- **LinkedIn** : [Ton Profil LinkedIn](https://www.linkedin.com/in/tonprofil)

---

### 💡 Inspirations et évolutions futures :
Ce projet est inspiré par les travaux de **Fisher** (1936) sur la classification des fleurs d'Iris. Bien que simple, il démontre la puissance des modèles de machine learning pour résoudre des problèmes pratiques. Dans le futur, ce projet pourrait évoluer en ajoutant de nouveaux modèles de classification, des jeux de données plus complexes, ou des fonctionnalités permettant d'explorer d'autres algorithmes d'IA.

Nous vous encourageons à explorer le code source sur **GitHub** et à contribuer à ce projet si vous le souhaitez !

---

Merci d'avoir pris le temps de découvrir ce projet. J'espère qu'il vous aidera à mieux comprendre les bases du machine learning et à vous amuser avec les fleurs d'Iris ! 🌸

""")

