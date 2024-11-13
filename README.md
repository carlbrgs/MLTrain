# Classification des Genres Musicaux avec un Arbre de Décision

## Objectif du Projet
Le but de ce projet est de prédire le **genre musical** d'une chanson en fonction de ses caractéristiques audio. Nous utilisons un **arbre de décision** pour classifier les chansons selon leur genre en exploitant les données fournies dans le fichier `genres_v2.csv`, téléchargé depuis [Kaggle](https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify/data).
**Genre**:

```
X = spotifyData[['danceability', 'energy', 'key', 'loudness', 'mode', 
                 'speechiness', 'acousticness', 'instrumentalness', 
                 'liveness', 'valence']]
```

## Données Utilisées
Les données contiennent diverses caractéristiques audio pour chaque chanson, telles que :
- **danceability** : Mesure de la facilité à danser sur la chanson.
- **energy** : Intensité et activité de la chanson.
- **key** : La tonalité musicale de la chanson.
- **loudness** : Le niveau de volume moyen de la chanson.
- **mode** : Mode musical, majeur ou mineur.
- **speechiness** : Mesure du caractère “parlé” de la chanson.
- **acousticness** : Probabilité que la chanson soit acoustique.
- **instrumentalness** : Niveau d'instrumentalité, ou absence de paroles.
- **liveness** : Probabilité que la chanson ait été enregistrée en direct.
- **valence** : Mesure de la positivité de la chanson.

La variable cible est le **genre** de chaque chanson, que nous essayons de prédire à partir de ces caractéristiques.

## Modèle Utilisé : Arbre de Décision
Nous avons choisi un **arbre de décision** pour son interprétabilité et sa simplicité. Un paramètre essentiel pour éviter le surajustement est la **profondeur maximale de l'arbre**, que nous avons fixée à 5 après plusieurs essais.

## Analyse des résultats
![image](https://github.com/user-attachments/assets/3d90df89-3a06-457d-8b53-6937d4495cf4)

- La précision globale du modèle sur l'ensemble de test est de 41.85%.
![image](https://github.com/user-attachments/assets/3cabbd5b-ce98-4060-8c9c-2b66af9b7344)
![image](https://github.com/user-attachments/assets/bdf26ed7-cd87-4536-b6a0-b94f5ca11ff5)G



- Les caractéristiques les plus importantes identifiées par l'arbre incluent danceability, energy, et loudness, ce qui suggère que ces aspects audio sont très influents pour différencier les genres.

