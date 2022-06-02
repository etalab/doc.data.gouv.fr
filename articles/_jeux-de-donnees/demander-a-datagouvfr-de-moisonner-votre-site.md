---
title: Demander à data.gouv.fr de moissonner votre site
slug: demander-a-datagouvfr-de-moissonner-votre-site
---

# Demander à data.gouv.fr de moissonner votre site

Si vous mettez en ligne des données publiques sur une plateforme ouverte et exposez les métadonnées dans l'un des [formats compatibles](#formats-de-métadonnées-compatibles), vous pouvez les référencer _automatiquement_ sur data.gouv.fr en utilisant notre service de moissonnage.

Le service de moissonnage permet de référencer sur data.gouv.fr des jeux de données publiés ailleurs sur le web. De cette manière, vous n’avez pas besoin d’importer à la main sur data.gouv.fr les jeux de données que vous avez déjà importés sur votre propre plateforme.

Un moissonneur permet d’importer toutes les données d’un portail d’open data. Vous pouvez aussi demander au moissonneur de n’importer que certains jeux de données, au moyen de filtres. Dit autrement, il n’est pas nécessaire de créer un moissonneur par jeu de données à importer sur data.gouv.fr, un seul moissonneur par portail suffit.

## Comment se déroule le moissonnage

1. Vous créez un moissonneur sur data.gouv.fr pour nous demander de surveiller votre plateforme ;
2. Vous publiez des données sur votre plateforme d’open-data sans vous préoccuper de data.gouv.fr ;
3. Vous demandez validation de votre moissonneur sur [le support data.gouv.fr](https://support.data.gouv.fr/collectivite-territoriale/referencement/moissonnage#support-tree) ;
4. La configuration du moissonneur est validée par l'équipe en charge de data.gouv.fr ;
5. Le moissonneur de data.gouv.fr vient automatiquement récupérer les données de votre plateforme ;
6. Les données de votre plateforme sont référencées et visibles sur data.gouv.fr.

Vous pouvez consulter [la documentation technique concernée]({{ site.baseurl }}{% link _moissonnage/intro.md %}) pour plus de détails

## Formats de métadonnées compatibles

Les moissonneurs de data.gouv.fr ne fonctionnent qu’avec certains formats de métadonnées :

- [OpenDataSoft]({{ site.baseurl }}{% link _moissonnage/ods.md %}) ;
- [CKAN]({{ site.baseurl }}{% link _moissonnage/ckan.md %}) ;
- [DCAT]({{ site.baseurl }}{% link _moissonnage/dcat.md %}).

{% include alert.html content="<b>Attention</b>: [geo.data.gouv.fr](https://geo.data.gouv.fr) permettait de moisonner des données issues d'Inspire mais il n’est plus activement maintenu. <br>Plus d’informations à propos [de l’extinction de geo.data.gouv.fr sont disponibles ici](https://www.data.gouv.fr/fr/posts/extinction-de-geo-data-gouv-fr/).<br>Pour des alternatives, voir [la section de la documentation **Moissonnage vs. geo.data.gouv.fr**](/moissonnage/intro/#moissonnage-vs-geodatagouvfr)." %}

## Créer un moissonneur

La création d’un moissonneur sur data.gouv.fr nécessite la création d’un compte gratuit.

Pour créer un nouveau moissonneur :

1. [Connectez-vous à votre compte](https://www.data.gouv.fr/fr/login) ;
2. Rendez-vous sur [votre tableau de bord](https://www.data.gouv.fr/fr/admin/), en cliquant sur **Administration** en haut à droite de votre écran ;
3. Cliquez sur l’icône en forme de plus (`+`) qui se trouve à gauche de votre avatar ;
4. Cliquez sur **Un moissonneur**.

À partir de là, la création du moissonneur se déroule en 3 étapes.

### 1. Définir qui publie les données moissonnées

Une fois moissonnées, c’est-à-dire récupérées sur votre plateforme, vos données sont publiées sur data.gouv.fr. L’étape 1 vous permet de choisir le compte qui sera associé à la publication sur data.gouv.fr des données moissonnées sur votre site.

Il peut s’agir de :

- votre propre compte, pour une publication à titre individuel, sous votre propre nom ;
- le compte d’une organisation dont vous êtes membre, pour une publication à titre collectif.

Si vous êtes membre d’une organisation, nous vous conseillons de publier vos jeux de données en son nom. Une fois votre choix effectué, cliquez sur le bouton **Suivant** pour accéder à l’étape 2.

### 2. Configurer le moissonneur

L’étape 2 vous permet de configurer votre moissonneur. Cette étape est importante pour que les données récupérées par data.gouv.fr soient aussi complètes que celles publiées sur votre plateforme à l’origine.

#### Nom

Donnez un nom à votre moissonneur. Il s’agit d’une référence interne, qui vous permet de vous y retrouver si vous créez plusieurs moissonneurs. Le nom de votre moissonneur ne sera pas public.

- **Mauvais nom** : Moissonneur de mon portail
- **Bon nom** : Plateforme open data Grand Lyon

Le nom du moissonneur est obligatoire.

### Description

Vous pouvez ajouter des précisions sur votre moissonneur dans le champ description. Là encore, il s’agit d’une référence interne qui n’a de valeur que pour vous.

La description est facultative.

### URL

Saisissez ici l’URL du portail à moissonner. Il s’agit généralement de l’URL de la page d’accueil de votre portail d’open data. L’URL permet au moissonneur de parcourir et récupérer tous vos jeux de données.

- **Mauvaise source** : `data.angers.fr`
- **Bonne source** : `https://data.angers.fr`

L’URL est obligatoire.

### Implémentation

Choisissez ici le format des métadonnées associées aux jeux de données publiés sur votre plateforme. Ce format permet au moissonneur de savoir comment lire et interpréter vos métadonnées, pour bien les retranscrire sur data.gouv.fr.

Certaines implémentations permettent d'ajouter des filtres, dans le but d’inclure ou d’exclure certains jeux de données du moissonnage. (Consultez [la section dédié de la documentation de moissonnage]({{ site.baseurl }}{% link _moissonnage/intro.md %}#filtrage) ainsi que les filtres [spécifiques de votre implémentations]({{ site.baseurl }}{% link _moissonnage/intro.md %}#moissonneurs-disponibles))

Le type d’implémentation est obligatoire.

### Actif

Cochez la case pour que votre moissonneur se mette au travail dès qu’il aura été validé par l’équipe en charge de data.gouv.fr. Laissez-la décochée pour activer votre moissonneur à la main.

Ce champ est obligatoire.

Une fois tous les champs obligatoires remplis, cliquez sur le bouton **Suivant** pour terminer la création de votre moissonneur.

### 3. Demander la validation du moissonneur

Une fois votre moissonneur configuré, demandez validation de votre moissonneur sur [le support data.gouv.fr](https://support.data.gouv.fr/collectivite-territoriale/referencement/moissonnage#support-tree). Il va être examiné par l’équipe en charge de data.gouv.fr, pour vérifier qu’il est bien réglé. Si c’est le cas, le moissonneur sera validé et vous recevrez une notification.

De votre côté, vous pouvez vérifier que votre moissonneur moissonne correctement votre site. Pour ce faire :

1. Cliquez sur le bouton **Voir dans l’administration** une fois votre moissonneur créé ;
2. Cliquez sur le bouton **Prévisualiser** ;
3. Vérifiez que le moissonneur récupère bien des jeux de données.

Tant que votre moissonneur n’est pas validé, il ne référence aucun jeu de données sur data.gouv.fr.
