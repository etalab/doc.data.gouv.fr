---
title: Opendatasoft
order: 4
---

# Moissonnage Opendatasoft

## Opendatasoft

[Opendatasoft](https://www.opendatasoft.com) est un service en PaaS permettant de mettre en œuvre ce qu'on appelle un datastore et le portail de données associé.

Le moissonneur utilise l'API de chaque portail Opendatasoft pour récupérer les métadonnées.

## Spécifications techniques

Ce moissonneur attend l'URL racine de votre portail Opendatasoft. C'est bien l'URL publique (`https://data.ma-compagnie.com`) qui est attendue, et non l'URL noire Opendatasoft (`https://ma-compagnie.opendatasoft.com`).

**Attention**: Opendatasoft utilise le slug (la portion identifiant le jeu de données dans les URLs) comme identifiant technique. L'outil laisse la possibilité de changer ce slug ce qui pose un vrai problème de pérénité des identifiants. Ayez donc à l'esprit que ce changement d'identifiant créera des doublons au moissonnage.

### Inspire

Il est possible de filtrer les jeu de données identifiés comme venant d'Inspire par Opendatasoft (propriété `interop_metas.inspire`).
Pour cela il suffit de cocher ou non l'option **Inspire** du moissonneur.
Cela permettra d’éviter des doublons pour les jeux de données déjà moissonnés par ailleurs. Il n’y a pas de règle universelle à son usage, c’est du cas par cas et il est de votre responsabilité de vérifier si ces jeux de données sont déjà pris en charge par une autre source de moissonnage.

## Correspondance des champs du modèle

### Jeu de données

| | data.gouv.fr | Opendatasoft | Notes |
|-|--------------|--------------|-------|
| Title | `title` | `title` | |
| Acronyme | `acronym` | ❌ | |
| Description | `description` | `description` | HTML converti en Markdown |
| Mots-clés | `tags` | `keywords` + `themes` | |
| Licence | `license` | `license` | champ libre: deviné sinon `LOv2` |
| Couverture spatiale | `spatial` | ❌ | |
| Couverture temporelle | `temporal_coverage` | ❌ | |
| Fréquence de mise à jour | `frequency` | ❌ | |
{: .table }

#### Autres métadonnées

Certaines propriétés additionnelles sont conservées dans l'attribut `harvest` par soucis de traçabilité.
Les informations de date sont sauvegardées dans ces métadonnées.

| | data.gouv.fr `harvest` | Opendatasoft | Notes |
|-|-----------------------|--------------|-------|
| Identifiant distant | `harvest:remote_id` | `datasetid` | ⚠ Attention au changement |
| URL de consultation | `ods_url` | `site`/explore/dataset/`datasetid`/ | |
| Référence interne | `ods_reference` | `reference` |  |
| Présence de données | `ods_has_records` | `has_records` | |
| Données spatiales | `ods_geo` | `features.geo` | |
| Date de modification | `modified_at` | `metas.modified` | |
{: .table }

### Ressources

Il existe 3 types de ressources identifiés chez Opendatasoft :
- l'API de données qui donnera lieu à plusieurs ressource sur data.gouv.fr :
  - un export au format `CSV`
  - un export au format `JSON`
  - un export au format `GeoJSON` dans le cas de données spatiales
  - un export au format `Shapefile` dans le cas de données spatiales
- les pièces jointes (`attachments` dans l'API Opendatasoft) qui seront chacune reconnue comme une ressource
- les exports alternatifs (`alternative_exports` dans l'API Opendatasoft) qui seront chacun reconnu comme une ressource

## Contribuer

Le moissonneur Opendatasoft est publié sur github dans le plugin [`udata-ods`](https://github.com/opendatateam/udata-ods). Vous pouvez donc soumettre des améliorations ou signaler des anomalies.

