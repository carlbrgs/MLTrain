import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Données téléchargées via "https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify/data"
#Le but est d'identifier le genre des musiques en fonctions de leurs caractéristiques

spotifyData = pd.read_csv('genres_v2.csv', low_memory=False)

X = spotifyData[['danceability', 'energy', 'key', 'loudness', 'mode', 
                 'speechiness', 'acousticness', 'instrumentalness', 
                 'liveness', 'valence']]

Y = spotifyData['genre']
print(Y.unique())

# Définir la profondeur maximale de l'arbre
max_depth = 5
clf = DecisionTreeClassifier(max_depth=max_depth, random_state=42)

clf.fit(X, Y)

print(clf)

plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=Y.unique(), filled=True)
plt.show()

# ************* accuracy ************

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

clf.fit(X_train, Y_train)

Y_pred = clf.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")