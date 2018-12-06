---
title: Introduction
order: 1
---

# Introduction

{:.no_toc}

- TOC {:toc}

## Racine

Le point d’entrée racine de l’API est https://www.data.gouv.fr/api/1/.

Dans la suite de cette documentation, il y sera fait référence par `$API`.

## Authentification

De façon à pouvoir exécuter des opérations d’écriture, vous devez commencer par obtenir une [clé d’API](https://www.data.gouv.fr/fr/admin/me/#apikey) dans les paramètres de votre profil.

Cette clé doit être fournie dans l’entête HTTP `X-API-KEY` à chaque appel en écriture (`POST`,`PUT`, `PATCH` et `DELETE`).

## Autorisations

Les appels d’API sont soumis aux même permissions que l’interface web.

Par exemple, vous devez être membre d’une organisation pour modifier l’un de ses jeux de données.

## Formats de données

### Content-type

Les différents points d’entrée de l’API attendent du JSON (`application/json`) en entrée et renvoient du JSON en sortie. Les seules exceptions sont les points d’entrée qui gèrent l’upload de fichiers : ils acceptent du `multipart/form-data` et renvoient du JSON.

### Identifiants d’URL

À chaque fois que vous pouvez utiliser identifiant d’objet dans une URL de l’API, vous avez les choix suivants :

- l’identifiant technique permanent (**ex:** `5bbb6d6cff66bd4dc17bfd5a`)
- le slug (**ex:** `mon-dataset`)

Par exemple, un dataset `5bbb6d6cff66bd4dc17bfd5a` dont le slug est `mon-dataset`, vous pouvez accéder à l’URL `$API/datasets/<dataset>`, par:

- `$API/datasets/5bbb6d6cff66bd4dc17bfd5a`
- `$API/datasets/mon-dataset`

**Attention** toutefois, le slug d’un objet peut-être amené à changer si le producteur change le nom de l’objet alors que l’identifiant technique lui ne change jamais. Il est donc préférable d’utiliser les identifiants techniques dans les scripts qui doivent être durables et rejouables.

### Listes simples

Les listes simples sont renvoyées sous forme d’une liste JSON.

Par exemple, [la liste des types de réutilisations]({{ site.baseurl }}{% link _api/reference.md %}#/reuses/reuse_types):

```json
[
  { "id": "paper", "label": "Papier" },
  { "id": "application", "label": "Application" },
  { "id": "hardware", "label": "Objet connecté" },
  { "id": "api", "label": "API" },
  { "id": "visualization", "label": "Visualisation" },
  { "id": "post", "label": "Article de blog" },
  { "id": "news_article", "label": "Article de presse" },
  { "id": "idea", "label": "Idée" }
]
```

### Pagination

Certaines méthodes sont paginées et suivent le même modèle de pagination. La liste d’objets est encapsulée dans un objet `Page`.

Vous n’avez pas à calculer vous-même les pages précédentes et suivantes puisque les URL sont disponible dans la réponse dans les attributs `previous_page` et `next_page`. Ils seront définis à `null` si il n’y a pas de page précédente et/ou suivante.

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

### Gestion d’erreurs

La gestion d’erreur de l’API utilise les codes d’erreur HTTP standards :

- **400**: requête invalide
- **401**: authentification requise
- **403**: permissions insuffisantes
- **500**: erreur indéfinie côté serveur
- **502**: le serveur ne répond pas

Lorsque c’est possible, l’API répondra en JSON avec le format suivant :

```json
{
  "message": "un message d’erreur"
}
```

#### Support

Si vous n’arrivez pas à comprendre une erreur, que vous avez besoin de support et souhaitez contacter l’équipe de data.gouv.fr, pensez à fournir les éléments suivants :

- la requête HTTP effectuée (avec les entêtes HTTP)
- la réponse éventuelle du serveur (avec ses entêtes)
- la date et l’heure de la requête
- un peu de contexte sur la raison de cette requête, son cadre

Parfois, la réponse en erreur comprend une entête `X-Sentry-ID`. Pensez à fournir cet identifiant, il nous aidera de comprendre précisement ce qui ne va pas et, si c’est un bug, à le corriger.

## Documentation de référence

Vous pouvez consulter la documentation de référence complète de l’API [ici]({{ site.baseurl }}{% link _api/reference.md %})
