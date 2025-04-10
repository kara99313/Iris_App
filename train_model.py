import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import joblib

# Charger le jeu de données Iris
iris = datasets.load_iris()

# Créer un DataFrame avec les noms des caractéristiques
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Entraîner un modèle RandomForest
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Sauvegarder le modèle dans un fichier .pkl
joblib.dump(model, "iris_model.pkl")

