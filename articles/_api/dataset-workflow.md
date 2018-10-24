---
title: Gestion d’un jeu de données
order: 3
snippets_types:
    curl.sh:
        label: CURL
        syntax: bash
    httpie.sh:
        label: HTTPie
        syntax: bash
    py:
        label: Python
        syntax: python
    php:
        label: php
        syntax: php
    java:
        label: Java
        syntax: java
---

# Gestion d'un jeu de données par l'API
{:.no_toc}

Cette page documente les principales interactions que vous pouvez avoir avec un jeu de données par l'API.

Il est recommandé d'avoir lu [l'introduction]({{ site.baseurl }}{% link _api/intro.md %}) avant de consulter cette page.


* TOC
{:toc}


Tous les examples qui suivent sont réalisés avec un compte:
- qui est actif
- dont la clé d'API est `my-api-key`
- qui est membre d'une organization dont l'identifiant est `5bbb6d6cff66bd4dc17bfd5a`.

Les exemples portants sur un jeu de données existant utilisent l'identifiant `5bc04b2cff66bd680e499f4a`.
Ceux portants sur une ressource existante de ce jeu de données utilisent l'identifiant `54d47250-1daf-483b-965a-3013f8c76617`.

Pour simplifier la lecture de ces exemples, il y sera fait référence par les variables suivantes pour chaque language:

{% snippets api/convention %}

## Création d'un jeu de données

Pour créer un jeu de données, nous allons utiliser l'API de [création de jeu de données]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/create_dataset).

{% snippets api/create-dataset %}

La réponse en JSON contient les metadonnées du jeu de données créé, en particulier l'identifiant et le slug.

La fiche du jeu de données est maintenant créée et il est maintenant possible d'y ajouter des ressources.

### Ajout d'une ressource

Pour créer une ressource, nous allons utiliser l'API  [création d'une ressource]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/create_resource).

Il existe 2 cas de création de ressource
- avec envoie d'un fichier, dit ressource locale
- avec référencement d'un fichier distant, dit ressource distante

#### En envoyant un fichier

Nous allons utiliser l'API d'[envoi de ressource]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/upload_new_dataset_resource) pour envoyer le fichier.

{% snippets api/upload-resource %}

La ressource est automatiquement créée et il est possible de modifier à posteriori les metadonnées avec l'[API de mise à jour de ressource]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/update_resource) comme décrit [plus bas](#mise-à-jour-des-métadonnées-dune-ressource)

#### En référençant une URL existante

L'API de [création de ressource]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/create_resource)  permet de créer une ressource distante.
Dans notre cas, un fichier csv hébergé sur l'URL https://url.to/ressource.csv.

{% snippets api/remote-resource %}

## Modification d'un jeu de données

La suite des opérations s'appliquent sur le même jeu de données dont l'identifiant est `5bc04b2cff66bd680e499f4a` sur lequel vous avez les permissions nécéssaires à la modification.
Ce jeu de données possède une ressource `54d47250-1daf-483b-965a-3013f8c76617` qui soit distante soit locale suivant les examples.


### Mise à jour des metadonnées de la fiche

Cette requête permet de mettre à jour les métadonnées d'un jeu de données en utilisant [l'API de mise à jour de jeu de données]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/update_dataset)

{% snippets api/update-dataset %}

### Mise à jour des métadonnées d'une ressource

Cette requête permet de mettre à jour les métadonnées d'une ressource en utilisant [l'API de mise à jour de ressource]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/update_resource)

{% snippets api/update-resource-meta %}

### Remplacer un fichier de ressource

Dans le cas d'une mise à jour de fichier de ressource locale (correction, ajout de données...),il est possible d'utiliser [l'API de mise à jour de fichier]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/upload_dataset_resource). L'ancien fichier sera toujours disponible pour ceux qui en dépendent mais la ressource affichée sur la page du jeu de données pointera vers le nouveau fichier.

{% snippets api/update-resource-file %}

### Signaler une mise à jour de fichier distant

Dans le cas d'une ressource distante, lorsque le fichier distant est mis à jour, il est important de le signaler afin que la fiche soit mise à jour et que les usagers le sache.

<center><strong>🚧 Bientôt 🚧</strong></center>
{% snippets api/update-remote-resource %}

### Suppression d'un ressource

[l'API de suppression de ressource]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/delete_resource) permet de supprimer une ressource de la fiche d'un jeu de données. Le fichier lui n'est pas supprimé afin de ne pas pénaliser ceux qui en dépendent.

{% snippets api/delete-resource %}

## Suppression d'un jeu de données

Pour supprimer un jeu de données, il suffit d'utiliser l'API de [suppression de jeu de données]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/delete_dataset):

{% snippets api/delete-dataset %}

Le jeu de données est maintenant **marqué comme supprimé**, il reste visible uniquement par vous et les membres de votre organisation,ainsi que par l'équipe d'administrateur de data.gouv.fr.
Il sera purgé (supprimé définitivement de la plateforme), d'ici la fin de la journée.

### Restauration d'un jeu de données supprimé par erreur

Tant que le jeu de donnéesn'a pas été purgé, vous avez la possibilité de le restaurer:

<center><strong>🚧 Bientôt 🚧</strong></center>
{% snippets api/restore-dataset %}
