---
title: Demander à data.gouv.fr de moissonner votre site
slug: demander-a-datagouvfr-de-moissonner-votre-site
---

# Demander à data.gouv.fr de moissonner votre site

Si vous mettez en ligne des données publiques sur une plateforme ouverte, dans un format dont les métadonnées correspondent à la syntaxe [ODS](https://www.opendatasoft.com), [CKAN](https://ckan.org), [DCAT](https://www.w3.org/TR/vocab-dcat/), ou MAAF (spécifique au ministère de l’agriculture), vous pouvez les référencer _automatiquement_ sur data.gouv.fr en utilisant notre service de moissonnage.

Le service de moissonnage permet de référencer sur data.gouv.fr des jeux de données publiés ailleurs sur le web. De cette manière, vous n’avez pas besoin d’importer à la main sur data.gouv.fr les jeux de données que vous avez déjà importés sur votre propre plateforme.

Un moissonneur permet d’importer toutes les données d’un portail d’open data. Vous pouvez aussi demander au moissonneur de n’importer que certains jeux de données, au moyen de filtres. Dit autrement, il n’est pas nécessaire de créer un moissonneur par jeu de données à importer sur data.gouv.fr, un seul moissonneur par portail suffit.

## Comment se déroule le moissonnage

1.  Vous créez un moissonneur sur data.gouv.fr pour nous demander de surveiller votre plateforme ;
2.  Vous publiez des données sur votre plateforme d’open-data sans vous préoccuper de data.gouv.fr ;
3.  Le moissonneur de data.gouv.fr vient automatiquement récupérer les données de votre plateforme ;
4.  Les données de votre plateforme sont référencées et visibles sur data.gouv.fr.

## Formats de métadonnées compatibles

Les moissonneurs de data.gouv.fr ne fonctionnent qu’avec certains formats de métadonnées :

-   Open Data Soft (ODS) ;
-   Comprehensive Knowledge Archive Network (CKAN) ;
-   Data Catalog Vocabulary (DCAT) ;
-   Ministère de l’agriculture, de l’alimentation, et des forets (MAAF).

## Créer un moissonneur

La création d’un moissonneur sur data.gouv.fr nécessite la création d’un compte gratuit.

Pour créer un nouveau moissonneur :

1.  [Connectez-vous à votre compte](https://www.data.gouv.fr/fr/login) ;
2.  Rendez-vous sur [votre tableau de bord](https://www.data.gouv.fr/fr/admin/), en cliquant sur votre nom et prénom, en haut à droite de votre écran, puis sur **Administration** ;
3.  Cliquez sur l’icône en forme de plus (`+`) qui se trouve à gauche de votre avatar ;
4.  Cliquez sur **Un moissonneur**.

À partir de là, la création du moissonneur se déroule en 3 étapes.

### 1. Définir qui publie les données moissonnées

Une fois moissonnées, c’est-à-dire récupérées sur votre plateforme, vos données sont publiées sur data.gouv.fr. L’étape 1 vous permet de choisir le compte qui sera associé à la publication sur data.gouv.fr des données moissonnées sur votre site.

Il peut s’agir de :

-   votre propre compte, pour une publication à titre individuel, sous votre propre nom ;
-   le compte d’une organisation dont vous êtes membre, pour une publication à titre collectif.

Si vous êtes membre d’une organisation, nous vous conseillons de publier vos jeux de données en son nom. Une fois votre choix effectué, cliquez sur le bouton **Suivant** pour accéder à l’étape 2.

### 2. Configurer le moissonneur

L’étape 2 vous permet de configurer votre moissonneur. Cette étape est importante pour que les données récupérées par data.gouv.fr soient aussi complètes que celles publiées sur votre plateforme à l’origine.

#### Nom

Donnez un nom à votre moissonneur. Il s’agit d’une référence interne, qui vous permet de vous y retrouver si vous créez plusieurs moissonneurs. Le nom de votre moissonneur ne sera pas public.

-   **Mauvais nom** : Moissonneur de mon portail
-   **Bon nom** : Plateforme open data Grand Lyon

Le nom du moissonneur est obligatoire.

### Description

Vous pouvez ajouter des précisions sur votre moissonneur dans le champ description. Là encore, il s’agit d’une référence interne qui n’a de valeur que pour vous.

La description est facultative.

### URL

Saisissez ici l’URL du portail à moissonner. Il s’agit généralement de l’URL de la page d’accueil de votre portail d’open data. L’URL permet au moissonneur de parcourir et récupérer tous vos jeux de données.

-   **Mauvaise source** :  `data.angers.fr`
-   **Bonne source** : `https://data.angers.fr`

L’URL est obligatoire.

### Implémentation

Choisissez ici le format des métadonnées associées aux jeux de données publiés sur votre plateforme. Ce format permet au moissonneur de savoir comment lire et interpréter vos métadonnées, pour bien les retranscrire sur data.gouv.fr.

Pour les données de type ODS et CKAN, vous pouvez aussi ajouter des filtres, dans le but d’inclure ou d’exclure certains jeux de données du moissonnage automatique. Peuvent faire l’objet de filtres : les éditeurs et les mots-clefs dans le cas d’ODS ; les organisations et les mots-clefs dans le cas de CKAN.

Le type d’implémentation est obligatoire.

### Actif

Cochez la case pour que votre moissonneur se mette au travail dès qu’il aura été validé par l’équipe en charge de data.gouv.fr. Laissez-la décochée pour activer votre moissonneur à la main.

Ce champ est obligatoire.

Une fois tous les champs obligatoires remplis, cliquez sur le bouton **Suivant** pour terminer la création de votre moissonneur.

### 3. Demander la validation du moissonneur

Une fois votre moissonneur configuré, ce dernier passe en attente de validation. Il va être examiné par l’équipe en charge de data.gouv.fr, pour vérifier qu’il est bien réglé. Si c’est le cas, le moissonneur sera validé et vous recevrez une notification.

De votre côté, vous pouvez vérifier que votre moissonneur moissonne correctement votre site. Pour ce faire :

1.  Cliquez sur le bouton **Voir dans l’administration** une fois votre moissonneur créé ;
2.  Cliquez sur le bouton **Prévisualiser** ;
3.  Vérifiez que le moissonneur récupère bien des jeux de données.

Tant que votre moissonneur n’est pas validé, il ne référence aucun jeu de données sur data.gouv.fr.
