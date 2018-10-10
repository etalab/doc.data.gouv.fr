---
title: Gestion d'un jeu de données
order: 3
snippets_types:
    sh:
        label: CURL
        syntax: console
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


## Convention

Tous les examples qui suivent sont réalisé avec un compte:
- un compte actif dont la clé d'API est `my-api-key`
- une organization dont l'identifiant est `5bbb6d6cff66bd4dc17bfd5a`.

Ils utilisent les conventions suivantes pour chaque language:

{% snippets convention %}

### CURL
{% highlight bash %}{% include_relative convention.sh %}{% endhighlight %}

### Python
{% highlight python %}{% include_relative convention.py %}{% endhighlight %}


## Création d'un jeu de données

Pour créer un jeu de données, nous allons utiliser successivement ces API:
- [création de jeu de données]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/create_dataset)
- [création d'une ressource]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/create_resource)
- [envoi d'une ressource]({{ site.baseurl }}{% link _api/reference.md %}#/datasets/upload_new_dataset_resource)

### CURL
{% highlight bash %}{% include_relative create-dataset.sh %}{% endhighlight %}

### Python
{% highlight python %}{% include_relative create-dataset.py %}{% endhighlight %}


## Modification d'un jeu de données

## Ajout d'une ressource distante

## Upload d'une ressource

## Mise à jour d'une ressource

## Suppression d'un ressource

## Supression d'un jeu de données
