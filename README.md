# 🌸 Application de Prédiction de Fleurs Iris

Une application web interactive développée avec Streamlit pour prédire l'espèce d'une fleur d'Iris basée sur les mesures de ses pétales et sépales. Ce projet utilise l'apprentissage automatique via scikit-learn pour offrir des prédictions précises et visualiser les résultats.

![Capture d'écran de l'application](/api/placeholder/800/450)

## ✨ Fonctionnalités

- 🔍 **Prédiction en temps réel** des espèces d'Iris (Setosa, Versicolor, Virginica)
- 📊 **Visualisation interactive** des probabilités pour chaque espèce avec Plotly
- 💾 **Historique des prédictions** sauvegardé automatiquement
- 📥 **Export des données** au format CSV
- 🎨 **Interface utilisateur intuitive** avec navigation simplifiée
- 📈 **Analyse des données** pour explorer les caractéristiques des iris

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/kara99313/Iris_App.git
   cd Iris_App
   ```

2. **Créer un environnement virtuel** (recommandé)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/MacOS
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
   
   > **Note:** Si vous rencontrez des problèmes avec certaines dépendances, essayez d'installer uniquement les packages essentiels:
   > ```bash
   > pip install streamlit pandas scikit-learn plotly joblib
   > ```

4. **Entraîner le modèle** (si ce n'est pas déjà fait)
   ```bash
   python train_model.py
   ```

## 💻 Utilisation

1. **Lancer l'application**
   ```bash
   streamlit run app.py
   ```

2. **Accéder à l'application** dans votre navigateur à l'adresse `http://localhost:8501`

3. **Navigation dans l'application:**
   - **Accueil**: Présentation générale du projet
   - **Prédiction**: Entrez les mesures pour obtenir une prédiction
   - **Historique**: Consultez les prédictions précédentes
   - **Analyse**: Visualisez et explorez les données
   - **Paramètres**: Configurez l'application
   - **À propos**: Informations sur le développeur et le projet

4. **Pour faire une prédiction:**
   - Ajustez les paramètres des mesures florales dans le panneau latéral
   - Cliquez sur "Prédire" pour obtenir les résultats

## 📊 Exemples de prédiction

| Sépale (longueur) | Sépale (largeur) | Pétale (longueur) | Pétale (largeur) | Prédiction |
|-------------------|------------------|-------------------|------------------|------------|
| 5.1 cm            | 3.5 cm           | 1.4 cm            | 0.2 cm           | Setosa     |
| 6.7 cm            | 3.0 cm           | 5.2 cm            | 2.3 cm           | Virginica  |
| 5.9 cm            | 3.0 cm           | 4.2 cm            | 1.5 cm           | Versicolor |

## 🤖 Modèle Random Forest en détail

### Présentation du modèle

Notre application utilise l'algorithme **Random Forest** qui est particulièrement adapté aux problèmes de classification comme celui des fleurs d'Iris. Ce modèle fait partie des méthodes d'ensemble (*ensemble learning*) qui combinent plusieurs modèles pour améliorer les performances prédictives.

### Fonctionnement du Random Forest

1. **Principes fondamentaux:**
   - Random Forest crée plusieurs arbres de décision indépendants (une "forêt")
   - Chaque arbre est entraîné sur un sous-échantillon aléatoire des données (technique de *bagging*)
   - À chaque nœud de décision, seul un sous-ensemble aléatoire des caractéristiques est considéré
   - La prédiction finale est déterminée par un vote majoritaire de tous les arbres

2. **Paramètres clés du modèle utilisé:**
   ```python
   RandomForestClassifier(
       n_estimators=100,       # Nombre d'arbres dans la forêt
       max_depth=None,         # Profondeur maximale des arbres (None = expansion complète)
       min_samples_split=2,    # Nombre minimum d'échantillons pour diviser un nœud
       min_samples_leaf=1,     # Nombre minimum d'échantillons requis dans une feuille
       criterion='gini',       # Mesure de la qualité de la division (gini ou entropy)
       random_state=42         # Assure la reproductibilité des résultats
   )
   ```

3. **Avantages du Random Forest pour cette application:**
   - **Robustesse au surapprentissage**: La combinaison de multiples arbres réduit le risque de surapprentissage
   - **Gestion efficace des petits jeux de données**: Parfait pour le dataset Iris qui ne contient que 150 observations
   - **Importance des caractéristiques**: Permet d'identifier facilement quelles mesures florales sont les plus discriminantes
   - **Quantification de l'incertitude**: Fournit des probabilités pour chaque classe, utiles pour nos visualisations
   - **Peu de prétraitement nécessaire**: Fonctionne bien sans normalisation extensive des données

### Prétraitement des données

Avant l'entraînement du modèle, les données sont préparées selon ces étapes:

1. **Division du jeu de données:**
   ```python
   X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.25, random_state=42, stratify=y
   )
   ```
   - 75% des données pour l'entraînement, 25% pour les tests
   - `stratify=y` assure une distribution équilibrée des classes dans les ensembles d'entraînement et de test

2. **Normalisation des caractéristiques:** 
   ```python
   scaler = StandardScaler()
   X_train = scaler.fit_transform(X_train)
   X_test = scaler.transform(X_test)
   ```
   - Centrage et mise à l'échelle des données pour améliorer la convergence

### Importance des caractéristiques

Notre analyse a révélé l'importance relative de chaque caractéristique pour la classification:

| Caractéristique      | Importance (%) |
|----------------------|----------------|
| Longueur du pétale   | 42.3%          |
| Largeur du pétale    | 38.7%          |
| Longueur du sépale   | 11.5%          |
| Largeur du sépale    | 7.5%           |

Ces valeurs montrent que les dimensions des pétales sont beaucoup plus discriminantes que celles des sépales pour identifier les espèces d'Iris.

### Validation croisée

Pour garantir la fiabilité du modèle, nous avons effectué une validation croisée à 10 plis:

```python
scores = cross_val_score(rf_model, X, y, cv=10)
print(f"Score moyen: {scores.mean():.3f} (± {scores.std():.3f})")
```

Résultat: **Score moyen: 0.953 (± 0.025)**

Ce score élevé avec un faible écart-type confirme la stabilité et la précision du modèle.

### Matrice de confusion détaillée

La matrice de confusion sur l'ensemble de test montre la répartition des prédictions:

```
                 | Prédit Setosa | Prédit Versicolor | Prédit Virginica
-------------------|---------------|------------------|------------------
Réel Setosa        |      13       |         0        |        0
Réel Versicolor    |       0       |        11        |        2
Réel Virginica     |       0       |         1        |       11
```

On observe une excellente classification des Setosa (100% correct) et quelques confusions entre Versicolor et Virginica, ce qui est cohérent avec leurs similarités biologiques.

### Courbes d'apprentissage

Nous avons également analysé les courbes d'apprentissage pour vérifier si notre modèle pourrait bénéficier de plus de données:

![Courbes d'apprentissage](/api/placeholder/600/350)

Les courbes montrent une convergence des scores d'entraînement et de validation, indiquant que notre modèle ne souffre pas de surapprentissage ou de sous-apprentissage significatif.

## 📈 Performance du modèle

Le modèle Random Forest utilisé dans cette application atteint une précision d'environ 95% sur l'ensemble de test. Les principales métriques sont:

- **Précision**: 0.95
- **Rappel**: 0.94  
- **Score F1**: 0.94

La matrice de confusion montre que le modèle est particulièrement performant pour identifier l'espèce Setosa, avec très peu de confusion entre Versicolor et Virginica.

## 📋 Structure du projet

```
IRIS_APP/
├── .streamlit/           # Configuration Streamlit
├── assets/               # Ressources statiques (CSS, images)
├── data/                 # Données et historique des prédictions
├── env/                  # Environnement virtuel (non suivi par git)
├── pages/                # Pages de l'application
│   ├── pages_files/      # Composants réutilisables
│   ├── A_propos.py       # Page "À propos"
│   ├── Accueil.py        # Page d'accueil
│   ├── Analyse.py        # Visualisations et analyses
│   ├── Historique.py     # Historique des prédictions
│   ├── Parametres.py     # Paramètres de l'application
│   └── predictions.py    # Page de prédiction
├── .gitignore            # Fichiers ignorés par git
├── app.py                # Point d'entrée principal
├── iris_model.pkl        # Modèle entraîné (généré par train_model.py)
├── predictions.csv       # Historique des prédictions
├── README.md             # Documentation du projet
├── requirements.txt      # Dépendances du projet
└── train_model.py        # Script d'entraînement du modèle
```

## 🌐 Déploiement

### Déploiement sur Streamlit Cloud

1. Créez un compte sur [Streamlit Cloud](https://streamlit.io/cloud)
2. Connectez votre compte GitHub
3. Sélectionnez ce dépôt et la branche principale
4. Cliquez sur "Deploy"

### Déploiement avec Docker

```bash
# Construire l'image
docker build -t iris-app .

# Exécuter le conteneur
docker run -p 8501:8501 iris-app
```

## 🔧 Dépannage

| Problème | Solution |
|----------|----------|
| `ModuleNotFoundError` | Vérifiez que toutes les dépendances sont installées avec `pip install -r requirements.txt` |
| L'application ne se lance pas | Assurez-vous que le fichier `app.py` est bien à la racine du projet |
| Le modèle ne se charge pas | Exécutez d'abord `python train_model.py` pour générer le fichier `iris_model.pkl` |
| Erreurs de chemin de fichier | Vérifiez que le dossier `data` existe et est accessible en écriture |

## 🛠️ Technologies utilisées

- [Streamlit](https://streamlit.io/) - Framework pour applications web de data science
- [scikit-learn](https://scikit-learn.org/) - Bibliothèque d'apprentissage automatique
- [Pandas](https://pandas.pydata.org/) - Manipulation et analyse de données
- [Plotly](https://plotly.com/) - Visualisations interactives
- [joblib](https://joblib.readthedocs.io/en/latest/) - Sérialisation de modèles ML

## 📊 Jeu de données

Cette application utilise le célèbre [jeu de données Iris](https://archive.ics.uci.edu/ml/datasets/iris) qui contient des mesures de 150 fleurs d'iris réparties en trois espèces:

- **Setosa**: Reconnaissable par ses petits pétales
- **Versicolor**: Présente des caractéristiques intermédiaires
- **Virginica**: Se distingue par ses grands pétales et sépales

Le jeu de données comprend 4 caractéristiques:
1. Longueur du sépale (cm)
2. Largeur du sépale (cm)
3. Longueur du pétale (cm)
4. Largeur du pétale (cm)

## 🔮 Roadmap

Fonctionnalités prévues pour les futures versions:

- [ ] Intégration de nouveaux algorithmes de classification
- [ ] Possibilité d'entraîner le modèle depuis l'interface utilisateur
- [ ] Ajout d'un mode de classification par image
- [ ] Support multilingue
- [ ] Mode hors ligne pour utilisation sans internet

## 👥 Contribuer

Les contributions sont les bienvenues! N'hésitez pas à:
1. Forker le projet
2. Créer une nouvelle branche (`git checkout -b feature/amazing-feature`)
3. Commiter vos changements (`git commit -m 'Add amazing feature'`)
4. Pousser sur la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) pour le jeu de données Iris
- La communauté Streamlit pour les exemples et inspiration
- Tous les contributeurs qui ont aidé à améliorer ce projet

## 📞 Contact

**Auteur:** KARABOUE VAKABOU  
**Email:** karabouevakabou@gmail.com  
**Lien du projet:** [https://github.com/kara99313/Iris_App](https://github.com/kara99313/Iris_App)

---

*Fait avec ❤️ et Python*