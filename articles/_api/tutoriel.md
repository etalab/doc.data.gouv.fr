---
title: Tutoriel
order: 2
---

# Tutoriel

Tous les exemples utilisent [httpie](http://httpie.org/) et [jq](http://stedolan.github.io/jq/) pour faciliter la lisibilité. Vous n'êtes pas contraint d'utiliser ces bibliothèques pour votre code, ce sont juste des outils pour mieux comprendre l'API.

## Vérifier que httpie fonctionne

Une fois httpie installé, vous pouvez vérifier qu'il fonctionne comme convenu en tapant cette commande dans votre terminal :

```console
$ http 'https://www.data.gouv.fr/api/1/organizations/?page_size=1'
```

Cela doit retourner une réponse de ce style :

```json
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
... LOTS OF HEADERS ...

{
    "data": [
        {

            ... LOTS OF DATA ...

            "name": "mairie de toulon",
            "page": "https://www.data.gouv.fr/organizations/mairie-de-toulon/",
            "slug": "mairie-de-toulon",
            "uri": "https://www.data.gouv.fr/api/1/organizations/5ba0b9f5634f4150f31579dd/",
            "url": "https://toulon.fr/"
        }
    ],
    "next_page": "https://www.data.gouv.fr/api/1/organizations/?page=2&page_size=1",
    "page": 1,
    "page_size": 1,
    "previous_page": null,
    "total": "10"
}
```

C’est très verbeux et nous n'avons pas besoin de toute cette information pour l'instant. C’est la raison pour laquelle nous utilisons jq.

## Vérifier que jq fonctionne

Une fois jq installé, vous pouvez vérifier qu'il fonctionne en tapant cette commande dans votre terminal :

```console
$ http 'https://www.data.gouv.fr/api/1/organizations/?page_size=1' | jq '.data[].name'
```

Cela doit retourner une réponse de ce style :

```json
"mairie de toulon"
```

C’est bien mieux ! Maintenant que tout fonctionne bien, réduisons un peu la taille de notre ligne de commande :

```console
$ export API="https://www.data.gouv.fr/api/1/"
```

La commande précédente est maintenant équivalente à la commande plus lisible (ne pas oublier les apostrophes) :

```console
$ http $API'organizations/?page_size=1' | jq '.data[].name'
```

C’est un bon début, maintenant plongeons dans l'API en elle-même. Nous ne le savons pas encore mais nous avons déjà récupéré notre première organisation.

## Parcourir et récupérer des données

Vous pouvez récupérer une liste d'organisations (filtrée ou non) ou une organisation unitaire. Lorsque vous récupérez un point d'accès, le nombre d'éléments par page par défaut est de 20. Récupérons les 20 premières organisations via l'API :

```console
$ http $API'organizations/' | jq '.data[].name'
```

```json
"mairie de toulon"
"SMIC DES VOSGES"
"Mairie de Vif"
"Kammoun nassib"
"Communauté urbaine de Caen la mer"
"Reno Inc"
"BEAUTEBOUTIQUE"
"Blue Soft"
"Syndicat de collecte et de traitement des déchets ménagers de l'Aude"
"Et voilà !"
```

C’est une bonne chose d'avoir cette liste mais que se passe-t-il si nous souhaitons parcourir les organisations retournées ? Récupérons les 5 premières URI d'organisations.

```console
$ http $API'organizations/?page_size=5' | jq '.data[].uri'
```

```json
"https://www.data.gouv.fr/api/1/organizations/5ba0b9f5634f4150f31579dd/"
"https://www.data.gouv.fr/api/1/organizations/5b9fbf32634f4128317ef388/"
"https://www.data.gouv.fr/api/1/organizations/5b9b657a634f412c7f5c939b/"
"https://www.data.gouv.fr/api/1/organizations/5b9ad48e634f413f7e0f3512/"
"https://www.data.gouv.fr/api/1/organizations/5b9a00938b4c41453e8a406b/"
```

Maintenant, nous sommes capables de récupérer une organisation seulement via l'URI retournée.

```console
$ http $API'organizations/5ba0b9f5634f4150f31579dd/' | jq '.'
```

Cela fait beaucoup de données à parcourir. Affinons ces données, si nous voulons seulement extraire les métriques :

```console
$ http $API'organizations/5ba0b9f5634f4150f31579dd/' | jq '.metrics'
```

```json
{
 "datasets": 0,
 "members": 1,
 "views": 1,
 "permitted_reuses": 0,
 "reuses": 0,
 "dataset_views": 0,
 "reuse_views": 0,
 "followers": 0,
 "resource_downloads": 0,

}
```

Ou peut-être juste le nom des membres de cette organisation :

```console
$ http $API'organizations/5ba0b9f5634f4150f31579dd/' | jq '.members[].user.last_name'
```

```json
"VOIRIN"
```

Il est vraiment de votre ressort de récupérer les données pertinentes pour votre projet. N'hésitez pas à consulter le [tutoriel de jq](http://stedolan.github.io/jq/tutorial/) et [son manuel](http://stedolan.github.io/jq/manual/) si vous voulez parcourir l'API via la ligne de commande plus en détail.

## Modifier et supprimer des données

Attention, vous entrez dans une zone de danger. Les modifications et suppressions de données via l'API sont définitives et nous ne proposons pas de bac à sable pour faire des tests avant de les exécuter (pour l'instant). Soyez conscient de ces responsabilités avant d'utiliser vos super pouvoirs.

Si vous tentez de modifier une ressource sans le token d'authentification, une erreur 401 sera renvoyée :

```console
$ http PUT $API'organizations/organization-uri-x/'
```

```json
HTTP/1.1 401 UNAUTHORIZED
... LOTS OF HEADERS ...

{
    "message": "Unauthorized",
    "status": 401
}
```

Vous devez spécifier votre Clé d'API (voir ci-dessus) et utiliser le header HTTP `X-API-KEY`. Si vous tentez de modifier une ressource que vous ne contrôlez pas, une erreur 400 sera retournée :

```console
$ http PUT $API'organizations/organization-uri-x/' X-API-KEY:your.api.key.here
```

```json
HTTP/1.1 401 UNAUTHORIZED
... LOTS OF HEADERS ...

{
    "message": "Invalid API Key",
    "status": 401
}
```

C’est le message que vous obtiendrez si vous avez spécifié une mauvaise clé d'API. C’est un autre message d'erreur potentiel que vous pouvez rencontrer.

```json
HTTP/1.1 403 FORBIDDEN
... LOTS OF HEADERS ...

{
    "message": "You do not have the permission to modify that object.",
    "status": 403
}
```

Cela arrive si vous essayez d'accéder à une ressource que vous ne pouvez éditer avec vos accréditations. Si votre clé est valide vous devriez obtenir quelque chose comme ça:

```json
HTTP/1.1 200 OK
... LOTS OF HEADERS ...

{
    ...
}
```

Mais ça ne change pas tout ! C’est parfaitement normal, nous avons oublié de spécifier la bonne donnée à envoyer au serveur.

```console
$ http PUT $API'organizations/organization-uri-x/' \
    X-API-KEY:your.api.key.here \
    name="Lorem ipsum" \
    description="The quick brown fox jumps over the lazy dog." \
    | jq '{name: .name, description: .description}'
```

```json
{
  "name": "Lorem ipsum",
  "description": "The quick brown fox jumps over the lazy dog."
}
```

La ressource a été modifiée avec vos nouvelles valeurs. Finalement, vous pouvez supprimer une ressource avec le verbe HTTP approprié (attention, aucun retour arrière n'est possible en utilisant l'API pour le moment):

```console
$ http DELETE $API'organizations/organization-uri-x/' X-API-KEY:your.api.key.here
```

```http
HTTP/1.0 204 NO CONTENT
... LOTS OF HEADERS ...
```

Une fois effectué, vous pouvez vérifier que c’est effectif en envoyant un GET sur l'URL précédente:

```console
$ http GET $API'organizations/organization-uri-x/'
```

```json
HTTP/1.0 410 GONE
... LOTS OF HEADERS ...

{
    "message": "Organization has been deleted",
    "status": 410
}
```

Consultez la [documentation de référence]({{ site.baseurl }}{% link _api/reference.md %}) pour d'autres intéractions avec l'API ou posez-nous vos questions sur le sujet !
