---
title: Publier un profil d’acheteur public
slug: publier-profil-acheteur
redirect_from: /faq/profils-d-acheteur.html
---

# Déclaration d’un profil d’acheteur

## Qui doit déclarer

La déclaration du profil d’acheteur est effectuée par l’acheteur, ou toute personne habilitée par celui-ci, sur [data.gouv.fr](https://data.gouv.fr)). L’objectif est d’impliquer les **éditeurs** de profils d’acheteurs afin de simplifier la déclaration des profils d’acheteurs initialement confiée aux acheteurs publics. Dans le cas où l’éditeur n’est pas en mesure d’assurer la déclaration, l’administrateur du profil d’acheteur ou l’acheteur peut le faire directement.

## Comment déclarer

### Format de fichier

Les éditeurs de profil d’acheteur sont invités à créer un fichier au format CSV contenant les informations suivantes :

- le SIRET des acheteurs (colonne `siretAcheteur`) ;
- l’adresse URL des profils d’acheteurs (colonne `urlProfilAcheteur`) ;
- l’adresse URL du catalogue DCAT qui répértorie les données (colonne `urlDCAT`) ;
- les coordonnées du ou des acheteurs concernés (colonne `coordonnees`).

Un modèle de fichier CSV est disponible [sur data.gouv.fr](https://www.data.gouv.fr/fr/datasets/structure-du-fichier-de-declaration-de-profil-dacheteur/#).

### Dépôt sur data.gouv.fr

Pour chaque fiche publiée il est essentiel de demander aux éditeurs de profils d’acheteurs d’associer le mot-clé (« tag ») suivant : « decp » (données essentielles de la commande publique) afin de permettre la centralisation de l’ensemble des contributions par Etalab.

La procédure complète pour déposer un ficher de déclaration de profil d’acheteur sur data.gouv.fr est la suivante :

1. Créer un compte individuel en allant sur : <https://www.data.gouv.fr/fr/register> ;
2. Une fois celui-ci validé via l’email de confirmation, créer une organisation correspondant à votre profil d’acheteur depuis : <https://www.data.gouv.fr/fr/admin/organization/new/> ;
3. Créer un jeu de données depuis <https://www.data.gouv.fr/fr/admin/dataset/new/> en choisissant lors de l’étape « Choisissez qui publie » l’organisation créée au point précédent ;
4. À l’étape « Décrivez votre jeu de données » renseigner un titre et éventuellement d’autres métadonnées (couverture spatiale, fréquence de mise à jour…) et **renseigner le tag (mot clé) « decp »** ;
5. À l’étape « Ajouter vos premières ressources » de la création du jeu de données, déposer le fichier CSV.
