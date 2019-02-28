---
title: CKAN
order: 3
---

# Moissonnage CKAN

## CKAN

[CKAN](https://ckan.org) est un logiciel libre permettant de mettre en oeuvre des portails de données.

Le moissonneur utilise l'API de CKAN pour récupérer les métadonnées.

## Spécifications techniques

Ce moissonneur attends l'URL racine de l'instance CKAN et non du portail (dans le cas où CKAN est couplé à Drupal par exemple).

Comme le moissonneur utilise l'API de CKAN, il nécéssite que celle-ci soit accessible.

Ce moissonneur n'est pas compatible avec les changements de modèles qui peuvent être effectué par certains plugins. Les champs d'un jeu de données doivent rester les même, et le format de leur contenu aussi.

Les champs additionnels du modèle sont ignorés.

## Correspondance des champs du modèle

### Jeu de données

La notion équivalente au jeu de données sur Data.gouv.fr (`Dataset`) est le `Package` dans CKAN.

| | Data.gouv.fr | CKAN | Notes |
|-|--------------|------|-------|
| Slug | `slug` | `name` | Création uniquement, si disponible |
| Titre | `title` | `title` ||
| Acronyme | `acronym` | ❌ ||
| Description | `description` | `notes` ||
| Mots-clés | `tags` | `tags.name` | |
| Date de création | `created_at` | `metadata_created` | |
| Date de mise à jour | `last_modified` | `metadata_modified` | |
| Licence | `license` | `license_id` et `license_title` | deviné |
| Couverture spatiale | `spatial` | `extras.spatial` et `extras.spatial-test` | deviné |
| Couverture temporelle | `temporal_coverage` | `extras.temporal_start` et `extras.temporal_end` ||
| Fréquence de mise à jour | `frequency` | `extras.frequency` | [Dublin Core Frequency](http://dublincore.org/groups/collections/frequency/) |
{: .table }

#### Extras

Certains champs sont conservés dans les attributs clés-valeurs `extras` par soucis de traçabilité:

| | Data.gouv.fr `extras` | CKAN | Notes |
|-|-----------------------|------|-------|
| Identifiant distant | `harvest:remote_id` | `id` | |
| Slug | `ckan:name` | `name` | Car `slug` peut déjà être pris |
| URL de consultation | `remote_url` | `url` | Conservé dans `ckan:source` si URL invalide |
{: .table }

Tous les attributs `extras` de CKAN qui ne font pas l'objet d'un traitement particulier, sont aussi conservés.

### Ressource

La notion équivaliente à la ressource sur Data.gouv.fr (`Resource`) est aussi la `Resource` dans CKAN.

| | Data.gouv.fr | CKAN | Notes |
|-|--------------|------|-------|
| Identifiant | `id` | `id` | Un UUID valide |
| Titre | `title` | `name` | |
| Description | `description` | `description` | |
| URL | `url` | `url` | |
| Type | `filetype` | `resource_type` | `api` ou `remote` |
| Type MIME | `mime` | `mimetype` | |
| Format | `format` | `format` | |
| Date de création | `created` | `created` | |
| Date de mise à jour | `modified` | `last_modified` | |
{: .table }


## Contribuer

Le moissonneur CKAN est publié sur github dans le plugin [`udata-ckan`](https://github.com/opendatateam/udata-ckan). Vous pouvez donc soumettre des améliorations ou signaler des anomalies.
