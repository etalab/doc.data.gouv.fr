---
title: Découvrir l’OpenData en tant que développeur
subtitle: "Comment interagir avec la plateforme ? Avec quelles API ?"
label: En tant que développeur
---

# Découvrir l’OpenData en tant que développeur

Cette page contient :

- [les informations relatives à l’API](#section-api) ;
- [le moissonnage des dépôts de données ouvertes](#section-moissonage) ;
- [le code source de la plateforme](#section-code).

<span id="section-api">
</span>

## Informations relatives à l’API

Le site « [data.gouv.fr](https://www.data.gouv.fr/) » propose différents moyens d’accéder au catalogue des données :

- une [API complète](https://www.data.gouv.fr/api/), documentée avec [Swagger](http://swagger.io/)
- des dumps au format CSV, mis à jour en temps réel

  - catalogue des jeux de données: <https://www.data.gouv.fr/datasets.csv>
  - catalogue des ressources: <https://www.data.gouv.fr/resources.csv>
  - catalogue des organisations: <https://www.data.gouv.fr/organizations.csv>
  - catalogue des réutilisations: <https://www.data.gouv.fr/reuses.csv>
  - une liste des tags avec leur nombre d’occurrences: <https://www.data.gouv.fr/tags.csv>

- un catalogue en rdf/DCAT-AP exposé dans plusieurs formats :

  - JSON-LD: <https://www.data.gouv.fr/catalog.jsonld>
  - Turtle: <https://www.data.gouv.fr/catalog.ttl>
  - N-Triples: <https://www.data.gouv.fr/catalog.nt>
  - XML-RDF: <https://www.data.gouv.fr/catalog.xml>
  - N3: <https://www.data.gouv.fr/catalog.n3>
  - Trig: <https://www.data.gouv.fr/catalog.trig>

- des [statistiques de fréquentation anonymisées](https://stats.data.gouv.fr/), mises à jour toutes les heures

L’intégralité des opérations réalisables depuis le site via votre navigateur peuvent être automatisées (publication d’un jeu de données, création d’organisations, etc). Veuillez consulter la documentation spécifique pour y accéder.

<span id="section-moissonage">
</span>

## Moissonnage des dépôts de données ouvertes

« [data.gouv.fr](https://www.data.gouv.fr/) » met à disposition une infrastructure de moissonnage, permettant d’être automatiquement intégré sur la plateforme.

Aujourd’hui, les moissonneurs suivants sont disponibles :

- CKAN (générique) ;
- OpenDataSoft (générique) ;
- DCAT-AP (générique) ;
- maaf (spécifique Ministère de l’Agriculture, de l’Agroalimentaire et de la Forêt).

Il est aussi possible d’écrire ses propres moissonneurs en suivant [la documentation spécifique](http://udata.readthedocs.io/en/stable/harvesting/#custom).

Le moissonnage n’est pas le seul moyen de synchroniser des données avec « data.gouv.fr », il est possible (voire recommandé) d’utiliser l’[API](https://www.data.gouv.fr/api/) pour pousser ses données.

<span id="section-code">
</span>

## Le code source de la plateforme

L’intégralité du code de la plateforme est [gratuitement disponible en Open-Source](https://github.com/opendatateam/udata) sous [licence AGPL3](https://www.gnu.org/licenses/agpl-3.0.html). Cet outil a été développé de façon modulaire pour permettre à tout un chacun de l’installer et de le personnaliser pour son usage propre en marque blanche. Nous avons par exemple développé les modules [udata-gouvfr](https://github.com/etalab/udata-gouvfr) pour le rendu et [udata-piwik](https://github.com/opendatateam/udata-piwik) pour les statistiques.

Vous pouvez contribuer en suivant la documentation spécifique et en proposant des _pull-requests_.
