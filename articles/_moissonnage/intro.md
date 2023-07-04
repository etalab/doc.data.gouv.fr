---
title: Introduction
order: 1
---

# 💡 Une nouvelle documentation est disponible ! 

[Découvrez la nouvelle version beta des guides et de la documentation de data.gouv.fr.](https://guides.data.gouv.fr/publier-des-donnees/guide-data.gouv.fr/moissonnage)

# Introduction

{:.no_toc}
- TOC
{:toc}

## Principe

Le moissonnage est une technique de récupération automatisée de metadonnées en "pull" : c'est le serveur data.gouv.fr qui va chercher les metadonnées sur les sites distants.

![Diagramme de séquence d'un moissonnage](/img/moissonnage/sequence.svg)


### Moissonnage vs. API

La publication par l'API vous donne un contrôle total sur le contenu de chaque champ, le moment de la soumission... tandis que le moissonnage, s'il ne nécessite pas de développement spécifique sur votre plateforme, est un fonctionnement fortement contraint.

| | Moissonnage | API |
|-|-------------|-----|
| Pré-requis | Métadonnées dans l'un des formats supportés | Capacité de développement |
| Déclenchement | Contrôlé par data.gouv.fr | Déclenché au besoin |
| Champs | Modèle imposé par protocole | Au choix du développeur |
{: .table }

### Moissonnage vs. geo.data.gouv.fr


{% include alert.html content="<b>Attention</b>: [geo.data.gouv.fr](https://geo.data.gouv.fr) n’est plus activement maintenu. <br> Plus d’informations à propos [de l’extinction de geo.data.gouv.fr sont disponibles ici](https://www.data.gouv.fr/fr/posts/extinction-de-geo-data-gouv-fr/)." %}

En plus du moissonnage et de l'utilisation de l'API, il existait un autre moyen automatisé de récupération des métadonnées sur data.gouv.fr : [geo.data.gouv.fr](https://geo.data.gouv.fr), anciennement inspire.data.gouv.fr.
Ce site pivot permettait de récupérer les métadonnées de jeux de données exposées selon [la directive européenne Inspire](https://inspire.ec.europa.eu) (obligation légale de publication des metadonnées geographiques selon le modèle de données **ISO 19115**, au format de données **ISO 19139**).

**Du fait de l'extinction à venir de la plateforme geo.data.gouv.fr, vous pouvez au choix**:

- attendre que le Geocatalogue publie directement des flux DCAT depuis vos flux Inspire
- si vous utilisez Geonetwork, utilisez [son endpoint DCAT alternatif](/moissonnage/dcat/#geonetwork)
- vous pouvez également utiliser [le moissonnage DCAT](/moissonnage/dcat) avec un grand nombre de logiciels compatibles ou avec un flux à façon
- enfin, nous supportons également le moissonnage des plateformes [CKAN](/moissonnage/ckan) et [OpenDataSoft](/moissonnage/ods)

### Moissonneurs disponibles

Aujourd'hui, data.gouv.fr peut moissonner les plateformes ou formats suivants :
- [DCAT](/moissonnage/dcat)
- [CKAN](/moissonnage/ckan)
- [DKAN, une variante du moissonneur CKAN](/moissonnage/ckan)
- [OpenDataSoft](/moissonnage/ods) ODS
- MAAF : un moissonneur spécifique au Ministère de l'Agriculture et de l'Alimentation

### Métadonnées communes

Les jeux de données moissonnés possèdent les attributs suivants dans leur champ `extras` pour la traçabilité :

| Attribut | Contenu |
|----------|---------|
| `harvest:domain` |	Nom de domaine moissoné |
| `harvest:source_id` | Identifiant technique du moissonneur |
| `harvest:remote_id` | Identifiant distant du jeu de données |
| `harvest:last_update` | Date du dernier moissonnage |
{: .table }


## Options

Chaque type de moissonneur possède des options spécifiques, ainsi que des options communes.
Aujourd'hui, la seule option commune est la possibilité de filtrage.

### Filtrage

La filtrage donne la possibilité d'inclure ou d'exclure un sous-ensemble de jeux de données du moissonnage.

Lorsqu'un ou plusieurs filtres sont déclarés, seuls les jeux de données remplissant **toutes** les conditions (**ET**) seront traités.


#### Portail multiproducteur : restriction à une organisation

![Exemple de restriction à une seule organisation](/img/moissonnage/harvest-filter-include.png)

#### Exclusion de mots-clés

![Exemple d'exclusion de mots-clés](/img/moissonnage/harvest-filter-exclude.png)

#### Combinaisons multiples

![Exemple de combinaison de filtres](/img/moissonnage/harvest-filter-combined.png)


## Rapport de moissonnage

Chaque moissonnage donne lieu à un rapport accessible depuis l'[interface d'administration de data.gouv.fr](https://www.data.gouv.fr/admin/).

Il vous permet de comprendre ce qu'il se passe et, le cas échéant, de corriger les erreurs existantes.
Il vous permettra aussi de vérifier que le filtrage se fait bien si vous en avez saisi un.

### Vue synthétique

![Vue synthétique du rapport de moissonnage](/img/moissonnage/admin-harvest-summary.png)

### Détails d'un jeu de données

![Détails d'un jeu de données du rapport de moissonnage](/img/moissonnage/admin-harvest-dataset-modal.png)

### En cas d'erreur

![Erreur sur un jeu de données du rapport de moissonnage](/img/moissonnage/admin-harvest-dataset-error-modal.png)

- **1** correspond à l'erreur **technique** formulée de façon compréhensible pour un humain
- **2** contient la "**stacktrace**" de l'erreur qui servira à ceux qui développent des moissonneurs ou contribuent aux existants.

## Limites

Le moissonnage n'a aucune connaissance de l'usage que vous faites du modèle de données. Il s'appuie uniquement sur les spécifications de chaque protocole ou plateforme pour récupérer les informations.

Il y a donc certaines limitations techniques liées aux spécificités de chaque plateforme (décrites sur la page de chaque moissonneur).

Certaines limitations sont communes et détaillées ci-dessous.

### Correspondances des métadonnées

Certains champs du modèle de data.gouv.fr possèdent un équivalent qui peut être sous-spécifis dans certains protocoles ou sur certaines plateformes, ou bien alors être spécifié différement, sur  plusieurs champs... Dans ce cas, la valeur du champ est récupérée en "best effort', c'est-à-dire qu'elle va être devinée en fonction des élements à disposition.
Se référer à la page de chaque moissonneur pour savoir lesquels sont dans ce cas pour chaque implémentation.

### Suppression à la source

Pour le moment, les moissonneurs ne gèrent pas la suppression à la source et ce pour éviter les suppressions en masse par erreur, ce qui entrainerait une perte des statistiques, des discussions et des ressources communautaires de chaque jeu de données.

Dans le cas d'une suppression ponctuelle, nous vous invitons à supprimer manuellement le jeu de données moissonné qui a perdu sa source.

Dans le cas d'une suppression massive de jeu de données, veuillez nous contacter afin de trouver une solution satisfaisante.

### Changement d'identifiant

Les moissonneurs utilisent les identifiants de jeu de données distants pour retrouver leurs données entre deux moissonnages. Il est donc important de veiller à ce qu'un jeu de données conserve son identifiant au fil du temps et des modification successives. Dans le cas contraire, cela donnera lieu à la création d'un doublon.

Il faut donc aussi veiller à ne pas supprimer puis recréer un jeu de données ou une ressource pour faire sa mise à jour.
