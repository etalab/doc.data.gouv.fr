---
title: Différences entre un jeu de données et une ressource
slug: difference-jeu-de-donnees-et-ressource
---

# Différences entre un jeu de données et une ressource

La plateforme data.gouv.fr permet de créer et de consulter des jeux de données. Un jeu de données se compose de ressources, de la même manière qu’un album est composé de chansons. Dit autrement, un jeu de données peut avoir plusieurs ressources et une ressource appartient nécessairement à un jeu de données.

À chaque jeu de données correspond une page de présentation sur data.gouv.fr, depuis laquelle peuvent être téléchargées les ressources qui y sont associées.

## Jeu de données

Un jeu de données comporte :

- un titre (obligatoire) ;
- un sigle (facultatif) ;
- une description (obligatoire) ;
- une licence (facultative) ;
- une fréquence de mise à jour (obligatoire) ;
- une date de dernière mise à jour (facultative) ;
- des mots-clefs (facultatifs) ;
- un intervalle de couverture temporelle (facultatif) ;
- une zone de couverture spatiale (facultative) ;
- un niveau de granularité spatiale (facultatif).

### Liens (URL)

Un jeu de données est référencé par au moins deux liens :
1. Lien avec un _slug_ (version « machine » du titre du jeu de données) : [https://www.data.gouv.fr/fr/datasets/resultats-des-elections-europeennes-2019/](https://www.data.gouv.fr/fr/datasets/resultats-des-elections-europeennes-2019/) ;
2. Lien avec un identifiant permanent : [https://www.data.gouv.fr/datasets/5ceba293634f411427c7d613](https://www.data.gouv.fr/datasets/5ceba293634f411427c7d613).

Le lien avec identifiant permanent ne change jamais pendant toute la durée de vie d'un même jeu de données. C'est la manière la plus fiable et la plus pérenne de partager le lien d'un jeu de données. L'identifiant permanent est accessible depuis l'onglet « Extras » dans l'encart bleu en haut de la page d'un jeu de données, à la ligne « ID ».

Le lien avec _slug_ change à chaque fois que le titre du jeu de données change. Toutefois, une redirection depuis l'ancien lien vers le nouveau est automatiquement créée quand le titre change.

## Ressources

Une ressource comporte :

- un titre (obligatoire) ;
- un type (obligatoire) ;
- une description (facultative) ;
- une date de publication (facultative) ;
- une URL (obligatoire) ;
- une taille en bytes (facultative) ;
- un format (obligatoire) ;
- un type mime (facultatif) ;
- une somme de contrôle (facultative).

### Liens (URL)

Une ressource est référencée par deux types de liens. Il s'agit de liens vers le fichier (ou l'API, la page...) en lui-même, i.e. le contenu de la ressource :
1. un lien direct qui peut changer quand une ressource est mise à jour : [https://static.data.gouv.fr/resources/fichier-consolide-des-bornes-de-recharge-pour-vehicules-electriques/20190805-140412/bornes-irve-20190805.csv](https://static.data.gouv.fr/resources/fichier-consolide-des-bornes-de-recharge-pour-vehicules-electriques/20190805-140412/bornes-irve-20190805.csv) ;
2. un lien stable (URL stable) qui ne change pas pendant tout le cycle de vie d'une même ressource : [https://www.data.gouv.fr/fr/datasets/r/50625621-18bd-43cb-8fde-6b8c24bdabb3](https://www.data.gouv.fr/fr/datasets/r/50625621-18bd-43cb-8fde-6b8c24bdabb3). Ce lien donne toujours accès à la dernière version du contenu de la ressource.

Ces différents liens sont accessibles après avoir déroulé l'encart d'une ressource depuis la page d'un jeu de données. Les liens sont presentés dans les informations au niveau des lignes « URL » et « URL stable ».
