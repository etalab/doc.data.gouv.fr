---
title: OpenDataSoft
order: 4
---

# Moissonnage OpenDataSoft

## OpenDataSoft

[OpenDataSoft](https://www.opendatasoft.com) est un service en PaaS permettant de mettre oeuvre ce qu'on appelle un datastore et le portail de données associé.

Le moissonneur utilise l'API de chaque portail OpenDataSoft CKAN pour récupérer les métadonnées.

## Spécifications techniques

## Correspondance des champs du modèle

| | Data.gouv.fr | ODS |
|-|--------------|-----|
| Licence | `license` | `license` |
| Couverture spatiale | `spatial` |  ❌ |
| Couverture temporelle | `temporal_coverage` | ❌ |
| Fréquence de mise à jour | `frequency` | ❌ |
{: .table }

## Contribuer

Le moissonneur OpenDataSoft est publié sur github dans le plugin [`udata-ods`](https://github.com/opendatateam/udata-ods). Vous pouvez donc soumettre des améliorations ou signaler des anomalies.

