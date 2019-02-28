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

| | Data.gouv.fr | CKAN |
|-|--------------|------|
| Licence | `license` | `license_id` et `license_title` |
| Couverture spatiale | `spatial` | `extras.spatial` et `extras.spatial-test` |
| Couverture temporelle | `temporal_coverage` | `extras.temporal_start` et `extras.temporal_end` |
| Fréquence de mise à jour | `frequency` | `extras.frequency` |
{: .table }

## Contribuer

Le moissonneur CKAN est publié sur github dans le plugin [`udata-ckan`](https://github.com/opendatateam/udata-ckan). Vous pouvez donc soumettre des améliorations ou signaler des anomalies.
