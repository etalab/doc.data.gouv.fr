---
title: Introduction
order: 1
---

# Introduction

## Racine

Le point d'entrée racine de l'API est <https://www.data.gouv.fr/api/1/>.

Dans la suite de cette documentation, il y sera fait référence par `$API_ROOT`.

## Authentification

De façon à pouvoir exécuter des opérations d'écriture, vous devez commencer par obtenir une [clé d'API](https://www.data.gouv.fr/fr/admin/me/#apikey) dans les paramètres de votre profil.

Cette clé doit être fournie à chaque appel dans l'entête HTTP `X-API-KEY`.

## Autorisations
Les appels d'API sont soumis aux même permissions que l'interface web.

Par exemple, vous devez être membre de l'organisation pour modifier l'un de ses jeux de données.

## Content-type

Les différents opints d'entré de l'API attende du JSON en entrée et renvoient du JSON en sortie.

## Pagination


## Documentation de référence

Le point d'entrée racine de l'API est <https://www.data.gouv.fr/apidoc/>.
