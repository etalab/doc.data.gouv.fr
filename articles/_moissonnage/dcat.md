---
title: DCAT
order: 2
---

# Moissonnage DCAT

## DCAT

[DCAT](https://www.w3.org/TR/vocab-dcat/) est une ontologie RDF pour décrire de jeux de données

L'Europe a publié sont extension de DCAT, appelée [DCAT-AP](https://joinup.ec.europa.eu/release/dcat-ap/11)

## Spécificités techniques

Ce moissonneur attend l'URL d'un **catalogue** DCAT.

Plusieurs format sont supportés:
  - `RDF XML`
  - `JSON-LD`
  - `Turtle`
  - `N3`
  - `NT`
  - `Trig`

La pagination est supporté via l'ontologie [Hydra](https://www.w3.org/community/hydra/wiki/Pagination) (ainsi que l'ancienne version)

## Correspondance des champs du modèle

| | Data.gouv.fr | DCAT |
|-|--------------|------|
| Licence | `license` | `dc:license` et `dc:right` depuis `dcat:distributions` |
| Couverture spatiale | `spatial` | ❌ |
| Couverture temporelle | `temporal_coverage` | `dct:temporal` |
| Fréquence de mise à jour | `frequency` | `dct:accrualPeriodicity` |
{: .table }

## Contribuer

Ce moissonneur fait partie du coeur de `udata`, [son code est disponible sur github](https://github.com/opendatateam/udata/blob/master/udata/harvest/backends/dcat.py). Vous pouvez donc soumettre des améliorations ou signaler des anomalies.
