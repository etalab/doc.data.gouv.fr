---
title: Découvrir l'OpenData en tant qu'intégrateur
subtitle: Quelles sont les intégrations tierces rendues possibles ?
label: En tant qu'intégrateur
summary: Quelles sont les intégrations tierces rendues possibles ?
---

# Découvrir l'OpenData en tant qu'intégrateur


La plateforme « [data.gouv.fr][] » vous offre plusieurs moyens plus ou moins avancés d’intégrer les données disponibles en open data sur vos propres sites :

1. de manière unitaire si vous souhaitez n’afficher qu’un ou quelques jeu(x) de données particulier(s) ;
1. de manière plus générale si vous souhaitez afficher tous les jeux de données
   relatifs à un territoire ou à une organisation ;
1. pour une gestion fine de l’habillage et des données affichées, nous vous recommandons l’API ;
1. pour avoir votre propre portail fondé sur le moteur de la plateforme.

Ces différents cas d’intégration correspondent généralement à différents profils :

1. un journaliste traitant d’une problématique donnée va être intéressé
   par l’inclusion de jeux de données directement au sein de sa page ;
1. une mairie va être intéressée par l’intégration des jeux de données relatifs
   à son territoire sur son site internet ;
1. une association pourrait être intéressée par la création d’une page personnalisée compilée
   à partir de données issues de sources multiples ;
1. un pays se lançant dans l’open data va chercher à créer son propre portail.

Quel que soit votre besoin ou votre profil,
nous sommes là pour vous accompagner dans votre démarche de diffusion de données ouvertes.
Ci-dessous, la documentation technique correspondant à chacun des cas évoqués :

## Intégration ponctuelle de jeux de données
Chaque jeu de données est intégrable sur n’importe quelle page en ajoutant deux lignes de HTML :

```html
<div data-udata-dataset="IDENTIFIANT DU JEU DE DONNÉES"></div>
<script src="https://www.data.gouv.fr/static/oembed.js" async defer></script>
```

En remplaçant `l’IDENTIFIANT DU JEU DE DONNÉES` par l’identifiant disponible sur sa page dédiée
vous devriez voir apparaître sur votre site un cartouche contenant les informations
relatives à ce jeux de données de la manière suivante :

![Exemple d'intégration d'une jeu de données](/img/faq/integration/exemple-dataset.png)
*Exemple d’intégration du jeu de données "Population" de l'INSEE.*

Il est possible d’intégrer plusieurs jeux de données à la fois en dupliquant la ligne correspondant à l’élément `<div>` avec un nouvel identifiant. Vous pouvez personnaliser l’apparence du rendu du cartouche grâce à la classe CSS `dataset-card`.

## Intégration d’une organisation

**Attention :** *ce type d’intégration est actuellement en cours de développement et l’API est susceptible de changer. Veuillez nous contacter si vous souhaitez participer aux tests préliminaires.*

Le mécanisme pour afficher tous les jeux de données relatifs à une organisation
est le même que celui pour l’intégration d’un seul jeu de donnée décrit précédemment.

Cet usage est recommandé si vous êtes responsable de cette organisation
et souhaitez faire la promotion des jeux de données associés.

```html
<div data-udata-organization="IDENTIFIANT DE L’ORGANISATION"></div>
<script src="https://www.data.gouv.fr/static/widgets.js" id="udata" async defer onload="udataScript.loadOrganization()"></script>
```
En remplaçant l’`IDENTIFIANT DE L’ORGANISATION` par l’identifiant disponible sur sa page dédiée
vous devriez voir apparaître sur votre site un cartouche contenant les informations relatives
aux jeux de données de cette organisation de la manière suivante :

Optionnellement, il est possible d’afficher une barre de recherche pour laisser la possibilité
au visiteur de filtrer la liste des jeux de données affichés.
Cela est activé en passant l’option `{withSearch: true}` à la méthode `loadOrganization()` ci-dessus.

![Exemple d'intégration d'une organisation](/img/faq/integration/exemple-organisation.png)
*Exemple d’intégration d'une organisation avec l'option barre de recherche.*

## Intégration pour une page personnalisée
Une [bibliothèque JavaScript][udata-js] a été développée pour faciliter la personnalisation
de l’affichage des jeux de données sur un site tiers.
Un système de gabarit permet d’intégrer les données que vous souhaitez issues de l’[API][]
à vos couleurs et selon la disposition qui vous convient.
Il s’agit d’un moyen de créer votre propre page open data à coûts réduits au sein de votre site.

## Intégration d’un portail open data complet
Les outils que nous développons sont disponibles en open-source.
Ils sont le fruit d’un effort international pour créer des synergies autour de la donnée ouverte
et mutualiser nos efforts de développement.
La gouvernance est inclusive et la licence est permissive.
Nous participons à l’animation autour du développement de la plateforme
car nous souhaitons produire un bien commun réutilisable par tous.

L’intégration d’un portail open data complet demande des compétences en administration système,
en développement Python et JavaScript ainsi qu’un temps non négligeable de prise en main de la plateforme.
C’est un choix qui doit être mûrement réfléchi
et nous vous recommandons de passer directement par « [data.gouv.fr][] »
si vous avez des données issues de territoires francophones.

Si vous souhaitez néanmoins vous lancer dans cette aventure, vous pouvez commencer par analyser
le [code source][udata-github] ainsi que la [documentation dédiée][udata-doc].
Vous pouvez également venir en [discuter avec la communauté][udata-gitter] (en anglais).

[data.gouv.fr]: https://www.data.gouv.fr
[API]: https://www.data.gouv.fr/fr/apidoc/
[udata-js]: https://github.com/DepthFrance/udata-js
[udata-doc]: http://udata.readthedocs.io/en/latest/
[udata-github]: https://github.com/opendatateam/udata
[udata-gitter]: https://gitter.im/opendatateam/udata
