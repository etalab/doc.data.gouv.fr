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

## Formats de données

### Content-type

Les différents points d'entrée de l'API attendent du JSON (`application/json`) en entrée et renvoient du JSON en sortie.
Les seules exceptions sont les points d'entrée qui acceptent l'upload de fichiers: ils acceptent du `multipart/form-data`et renvoie du JSON. 

### Listes

### Pagination

Certaines méthodes sont paginées et suivent le même modèle de pagination. La liste d'objets est encapsulée dans un objet `Page`.

Vous n'avez pas à calculer vous-même les pages précédentes et suivantes puisque les URL sont disponible dans la réponse dans les attributs `previous_page` et `next_page`. Ils seront définis à `null` si il n'y a pas de page précédente et/ou suivante.

**Exemple:**
```json
{
    "data": [{...}, {...}],
    "page": 1,
    "page_size": 20,
    "total": 10,
    "next_page": "https://www.data.gouv.fr/api/endpoint/?page=2",
    "previous_page": null
}
```

### Gestion d'erreurs

`X-Sentry-ID`

## Documentation de référence

Le point d'entrée racine de l'API est <https://www.data.gouv.fr/apidoc/>.
