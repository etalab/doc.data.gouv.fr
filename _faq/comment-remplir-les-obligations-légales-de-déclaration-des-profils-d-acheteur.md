---
title: >-
  Comment remplir les obligations légales des profils d'acheteur
  ?
subtitle: En tant qu'acheteur public
label: En tant qu'acheteur public
---

# Comment remplir les obligations légales des acheteurs publics ?

## Un peu de contexte

[L'arrêté du 14 avril 2017](https://www.legifrance.gouv.fr/eli/arrete/2017/4/14/ECFM1637256A/jo/texte), modifié par [l'arrêté du 27 juillet 2018](https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000037282994&dateTexte=&categorieLien=id), impose à tous les acheteurs publics la publication des données essentielles de la commande publique. Ainsi, à partir du 1er octobre 2018, les acheteurs publics doivent publier les données d'attribution au plus tard deux mois après la notification du marché.

La structure des données est définie par [des schémas XML et JSON](https://github.com/etalab/format-commande-publique) qui appliquent les exigences des arrêtés.

Pour plus d'information, vous pouvez consulter [la page thématique](https://www.economie.gouv.fr/daj/ouverture-des-donnees-commande-publique) sur le site de la Direction des Affaires Juridiques.

Les données essentielles publiées sur data.gouv.fr proviennent de trois sources :

- La **DGFiP (Direction générale des finances publiques)** propose aux acheteurs publics soumis à la comptabilité publics (par exemple les collectivités) de faire remonter ces données via Hélios ([PES Marché](https://www.collectivites-locales.gouv.fr/protocole-dechange-standard-pes-0)), pour ensuite les transmettre à la mission Etalab qui les met à disposition du public (voir ci-dessous).
- L'**AIFE (Agence Informatique des Finances de l'État)** publie sur [data.gouv.fr](https://data.gouv.fr) les données essentielles provenant de la plateforme de marchés de l'Etat, [PLACE](https://www.marches-publics.gouv.fr/?page=entreprise.AccueilEntreprise).
- Les données essentielles publiées sur les profils d'acheteurs (places de marché) peuvent être publiées sur data.gouv.fr via l'API data.gouv.fr ou via un fichier DCAT moissonnable

## Publication des données essentielles via l'API data.gouv.fr

La documentation de l'API est disponible [ici](https://www.data.gouv.fr/fr/apidoc), le détails des propriétés des jeux de données est [en bas de la même page](https://www.data.gouv.fr/fr/apidoc/#!/datasets/create_dataset).

Afin de faciliter la localisation et donc l'utilisation des données essentielles, la publication de ces données doit respecter une certaine structure. Les deux structures proposées sont les suivantes :

- structure **plateforme** : un jeu de données (`dataset` dans l'API) par plateforme de marchés (identifiée par son SIRET)
- structure **acheteur** : un jeu de données par acheteur public (SIRET)

### Jeu de données

Pour des raisons d'archivage, le téléversement des fichiers de données sur data.gouv.fr est fortement préféré par rapport à un lien vers des serveurs externes.

Une fois que le `Dataset` a été créé, vous pouvez y ajouter des `Ressource` ([API ressource](https://www.data.gouv.fr/fr/apidoc/#!/datasets/upload_new_dataset_resource)).

Exemple de commande :

```bash
curl --request POST --url https://data.gouv.fr/api/1/datasets/<dataset-id>/upload/ --header 'content-type: multipart/form-data' --header 'x-api-key: <api-key>' --form "file=<chemin du fichier à téléverser>"
```

#### Nom (`title` dans l'API)

Le nommage du jeu de données dépend de la structure choisie pour la publication :

- jeu de données pour une **plateforme** : Données essentielles des marchés publics - `{nom de la plateforme}`
- jeu de données pour un **acheteur** : Données essentielles des marchés publics - `{nom de l'acheteur}`

Exemple :

> Données essentielles des marchés publics - Conseil régional de Bretagne

#### Description (`description`)

La description attendue est un texte générique décrivant le contexte de publication des données essentielles ainsi que quelques liens utiles. Le texte suivant remplit ces conditions et peut être étendu par le producteur, notamment avec un lien vers l'interface de visualisaton de données du profil d'acheteur concerné.

```
[L'arrêté du 14 avril 2017](https://www.legifrance.gouv.fr/eli/arrete/2017/4/14/ECFM1637256A/jo/texte), modifié par [l'arrêté du 27 juillet 2018](https://www.legifrance.gouv.fr/affichTexte.do?cidTexte=JORFTEXT000037282994&dateTexte=&categorieLien=id), impose à tous les acheteurs publics la publication des données essentielles de la commande publique. Ainsi, à partir du 1er octobre 2018, les acheteurs publics doivent publier les données d'attribution au plus tard deux mois après la notification du marché.

La structure des données est définie par [des schémas XML et JSON](https://github.com/etalab/format-commande-publique) qui appliquent les exigences des arrêtés.

Pour plus d'informations, vous pouvez consulter [la page thématique](https://www.economie.gouv.fr/daj/ouverture-des-donnees-commande-publique) sur le site de la Direction des Affaires Juridiques.
```

#### Mot-clés (`tags`)

Renseignez le mot-clé `données-essentielles-commande-publique`.

#### Extras (`extras`)

Si le jeu de données est spécifique à un **acheteur** et non à une plateforme, ajoutez une propriété `siret` à la propriété `extras` de l'objet `Dataset`, et indiquez le SIRET de l'acheteur.

```
{
    "title": "Données essentielles des marchés publics - Conseil régional de Bretagne"
    ...
    "extras": {
        "siret": "89764547841001"
}
```

Si le jeu de données est spécifique à une **plateforme**, ne renseignez pas la propriété `extras`.

#### Licence (`license`)

La licence à renseigner est la [licence ouverte](https://www.etalab.gouv.fr/wp-content/uploads/2014/05/Licence_Ouverte.pdf) : `fr-lo`

#### Organisation (`organization`)

Ajoutez votre identifiant d'organisation data.gouv.fr. L'utilisateur qui publie les données doit appartenir à cette organisation.

#### Fréquence (`frequency`)

Renseignez la fréquence de la publication des mises à jour.

### Ressource

#### Nom du fichier

Format : DECP-`{SIRET}`-`{année}`-`{mois}`-`{jour}`-`{numéro de séquence}`.`{extension}`

- `DECP` pour "données essentielles de la commande publique"
- `siret` : SIRET de la plateforme si structure plateforme, sinon SIRET de l'acheteur
- `année` : année de la publication sur data.gouv.fr
- `mois` : mois de la publication sur data.gouv.fr
- `jour` : jour de la publication sur data.gouv.fr
- `numéro de séquence` : numéro de séquence du fichier à incrémenter si plusieurs fichiers sont publiées dans la même journée. Le premier numéro est `01`
- `extension` : `xml` ou `json` en fonction du format de publication. Il n'est pas obligatoire de publier les données à la fois en XML et en JSON, un seul des deux formats suffit.

Exemple :

> 89764547841001-2018-11-28-01.xml

#### URL (`url`)

L'URL n'est renseignée que si le fichier n'est pas téléversé sur data.gouv.fr et hébergé sur un serveur externe.

#### Nom (`title` dans l'API)

Identique au nom de fichier.

#### Type de fichier (`filetype`)

- `xml` pour du XML
- `json` pour du JSON

#### Type MIME (`mime`)

- `application/xml` pour du XML
- `application/json` pour du JSON

#### Type de ressource (`type`)

Renseignez `main`.


## Téléchargement des données essentielles transmises par la DGFiP via le PES Marché

### Via un système de fichier

Les données essentielles transmises par la DGFiP peuvent être téléchargées depuis leur emplacement sur un système de fichiers hébergé par Etalab. Cette méthode est particulièrement adaptée pour récupérer les données essentielles d'un acheteur qui passe beaucoup de marchés.


Le format des URL est le suivant :

http://files.data.gouv.fr/decp/{siret}/{année}/{mois}/{jour}/{siret}-{année}-{mois}-{jour}-{seq}.xml

- `siret` : SIRET de l'acheteur
- `année` : année de la récéption par Etalab
- `mois` : mois de la récéption par Etalab
- `jour` : jour de la récéption par Etalab
- `numéro de séquence` : numéro de séquence du fichier à incrémenter si plusieurs fichiers sont réceptionnés dans la même journée. Le premier numéro est `01`

Exemple :

> http://files.data.gouv.fr/decp/89764547841001/2018/11/28/89764547841001-2018-11-28-01.xml

### Via l'API

Cette méthode est particulièrement adaptée pour récupérer les données essentielles d'un acheteur qui ne passe pas beaucoup de marchés.

Pour récupérer les données via l'API, il vous faut :

1. Récupérer la liste des ressources du jeu de données
2. Télécharger les ressources dont vous avez besoin

#### Récupérer la liste des ressources du jeu de données

Pour récupérer la liste des ressources d'un jeu de données, effectuez la requête suivante :

```
curl https://data.gouv.fr/api/1/datasets/<dataset id ou slug>
```

Exemples d'URL :

> https://data.gouv.fr/api/1/datasets/56cc6d6988ee385864fa79d0
>
> https://data.gouv.fr/api/1/datasets/referentiel-de-donnees-marches-publics


## Déclaration d'un profil d'acheteur

La déclaration du profil d'acheteur est effectuée par l'acheteur ou toute personne habilitée par celui-ci sur le portail unique interministériel ([data.gouv.fr](https://data.gouv.fr)) destiné à rassembler et à mettre à disposition librement l'ensemble des informations publiques.

L'objectif est d'impliquer les éditeurs de profils d’acheteurs afin de simplifier et rationnaliser la déclaration des profils d'acheteurs initialement confiée aux acheteurs publics.

Les éditeurs de profil d'acheteur sont invités à se créer un compte sur la plateforme data.gouv.fr afin d'y publier au format .CSV un fichier contenant les informations suivantes :
  * le SIRET des acheteurs (colonne `siretAcheteur`)
  * l'adresse URL des profils d'acheteurs (colonne `urlProfilAcheteur`)
  * les coordonnées du ou des acheteurs concernés (colonne `coordonnnées`)

<strong>Pour chaque fiche publiée il est essentiel de demander aux éditeurs de profils d’acheteurs d’associer le mot clé (« tag ») suivant :
« DECP » (données essentielles de la commande publique) afin de permettre la centralisation de l’ensemble des contributions par Etalab.</strong>
