---
title: Licences
order: 5
---

# Détection des licences par le moissonnage

Lors du moissonnage, la liste de référence de data.gouv.fr — [disponible ici au format json](https://www.data.gouv.fr/api/1/datasets/licenses/) — est utilisée pour détecter la licence du jeu de données distant.

Cette détection utilise les attributs suivants :
- `id`
- `title`
- `alternate_titles`
- `url`
- `alternate_urls`

Le meilleur moyen d'assurer une compatibilité parfaite est d'utiliser l'`id` sur le flux distant lorsque c'est possible.
