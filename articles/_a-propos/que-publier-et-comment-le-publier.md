---
title: Que publier et comment le publier
slug: que-publier-et-comment-le-publier
---
# Que publier sur data.gouv.fr et comment le publier

data.gouv.fr est la plateforme ouverte des données publiques française. En ce sens, elle met en relation des producteurs et des utilisateurs de données. Une donnée est considérée comme ouverte quand elle peut être consultée, utilisée, et partagée par tous, sans restriction.

## Qui peut publier

Tout le monde peut publier des données sur data.gouv.fr, du moment qu’il s’agit de données d’intérêt public. Plus précisément, vous pouvez publier des données sur data.gouv.fr :

* Si vous produisez ou collectez des données dans le cadre d’une mission de service public, et si ces données ne contiennent pas d’informations personnelles et qu’elles ne révèlent pas de secrets.
* Si vous enrichissez ou complétez des données publiques pour le compte d’une association, d’un projet de recherche ou par simple curiosité, et si vos données sont d’intérêt public.

Par services publics, nous faisons référence aux services de l’État, c’est-à-dire :

* les ministères et les administrations centrales ;
* les services déconcentrés et les autorités indépendantes (préfectures, conseils supérieurs) ;
* les collectivités territoriales (villes, conseils généraux, conseils régionaux) ;
* les entreprises qui assurent une mission de service public (SNCF, RATP, Caisse des dépôts).

## Que publier

Vaste sujet. Pour commencer, nous vous conseillons de faire la distinction entre les jeux de données et les agrégats de documents isolés. Quelles différences entre un jeu de données et un document isolé ? Les jeux de données sont suffisamment volumineux et structurés pour être analysés par une machine, ce qui n’est pas toujours le cas des documents isolés. Dit autrement, mettre des informations sur internet ne suffit pas, hélas, encore faut-il que les informations mises en ligne soient ordonnées et lisibles par une machine — sans quoi elles ne pourront être utilisées.

Par exemple, le taux de réussite à l’examen du baccalauréat ne constitue pas un jeu de données. À l’échelle nationale, il s’agit d’un simple chiffre, un document isolé. En revanche, si un tableau Excel (ou un fichier CSV) contient le taux de réussite au baccalauréat de _tous_ les lycées français, on peut dans ces conditions commencer à parler de jeu de données, car ces données peuvent être croisées, recoupées avec d’autres données, dans le but de produire des analyses.

Un bon test pour vos données consiste donc à évaluer leur modularité : vos données peuvent-elles facilement être combinées avec d’autres jeux de données ? Par exemple, les données sur les dépenses de santé d’une région peuvent être combinées avec les données démographiques de cette même région dans le but d’évaluer l’efficacité des dépenses de santé sur ce territoire.

Si vous ne savez pas par où commencer, nous vous recommandons de faire simple, en commençant par des jeux de données faciles à rassembler et susceptibles d’intéresser le grand public.

Voici quelques exemples tout sauf exhaustifs :

* les mesures de qualité de l’air ;
* les adresses des services publics ;
* les statistiques du tourisme ;
* les résultats électoraux ;
* les horaires des transports publics ;
* les impôts et et le budget.

## Comment le publier

### Choisir un format de publication standardisé

Les données publiées sur data.gouv.fr ont vocation à être consultées et réutilisées. Pour que vos données puissent être réutilisées par des tiers, nous vous conseillons de les mettre en forme selon des standards ouverts et communément adoptés dans le secteur au sein duquel vous évoluez.

#### Données tabulaires

Les données tabulaires (feuilles de calcul), gagnent à être publiées sous la forme de fichiers CSV (_comma-separated values_), reconnaissables à leur extension en `.csv`. Si le fichier que vous avez entre les mains est un fichier Excel, nous vous conseillons d’exporter vos données au format CSV. [Voir comment exporter des données au format CSV à partir d’Excel](https://support.office.com/fr-fr/article/importer-ou-exporter-des-fichiers-texte-txt-ou-csv-5250ac4c-663c-47ce-937b-339e391393ba)

Pour le dire vite, les fichiers CSV sont des fichiers qui contiennent du texte et dans lequel les valeurs sont séparées par des virgules, ce qui permet facilement de les convertir en tableaux. Les CSV sont aux tableaux ce que les aliments lyophilisés sont à l’alimentation : un format qui nécessite peu d’efforts pour être assimilé.

Le fichier qui suit est un fichier CSV, les valeurs qu’il contient sont séparées par des virgules.

```
Pays, Capitale, Population, Langue
France, Paris, 67 795 000, français
Espagne, Madrid, 48 958 159, espagnol
Italie, Rome, 60 589 445, italien
Allemagne, Berlin, 82 800 000, allemand
```

Quand vous créez votre fichier CSV, nous vous conseillons de :

* utiliser la première ligne de votre fichier comme une en-tête descriptive ;
* séparer chacune de vos valeurs par une virgule, comme s’il s’agissait de colonnes ;
* vérifier que vous avez bien le même nombre de valeurs sur chaque ligne ;
* vérifier que votre fichier ne contient pas de lignes blanches, vides ;
* encoder votre fichier en UTF-8, pour éviter que vos caractères accentués deviennent des monstres.

#### Données de transport

Les données de transport gagnent à être publiées dans les formats suivant :

* GTFS ;
* NeTEx.

[Voir la documentation de transport.data.gouv.fr](https://transport.data.gouv.fr/guide)

#### Données géographiques

Les données géographiques gagnent à être publiées dans les formats suivant :

* GeoJSON, Shapefile, MapInfo MIF/MID, MapInfo TAB et GML, pour les vecteurs ;
* ECW, JPEG2000 et GeoTIFF, pour les données pixelisées (raster).

[Voir la documentation de geo.data.gouv.fr](https://geo.data.gouv.fr/fr/doc/publish-your-data)

#### Données hiérarchiques

Si vos données comportent une structure interne, qu’elles sont ordonnées, rangées, découpées en plusieurs objets, alors nous vous recommandons les formats suivants :

* JSON ;
* YAML ;
* XML.

#### Images et vidéo

Bien que data.gouv.fr soit théoriquement ouvert à toutes et à tous, nous ne pouvons pas accueillir les documents de tout le monde, surtout quand il s’agit de fichiers volumineux, comme les images et les vidéos. Nous vous conseillons d’héberger vous-même les images et les vidéos que vous jugez d’intérêt public avant de les référencer sur data.gouv.fr.

#### Autres types de données

Pour tous les autres types de données, nous vous conseillons de jeter un œil au [référentiel général d’interopérabilité](https://references.modernisation.gouv.fr/interoperabilite) (disponilbe au format PDF), qui référence les normes et les standards au sein des systèmes d’information de l’administration.

### Choisir une licence

Par défaut, les données publiées sur data.gouv.fr tombent sous le coup du [Code des relations entre le public et l'administration](https://www.legifrance.gouv.fr/affichCode.do;jsessionid=E4583EBE2857A0DF9056D5D0082F8F2D.tplgfr31s_2?idSectionTA=LEGISCTA000032255212&cidTexte=LEGITEXT000031366350&dateTexte=20181016), qui dispose notamment que :

> Les informations publiques figurant dans des documents communiqués ou publiés par les administrations (…) peuvent être utilisées par toute personne qui le souhaite à d'autres fins que celles de la mission de service public pour les besoins de laquelle les documents ont été produits ou reçus.

Si vous souhaitez être plus spécifique que le Code des relations entre le public et l'administration, vous pouvez choisir de publier vos données sous une licence ouverte. L’esprit des licences ouvertes reste le même que celui du Code des relations entre le public et l'administration, c’est-à-dire qu’il est toujours question que vos données puissent être librement consultées, réutilisées, et partagées, mais certaines licences introduisent des nuances, notamment sur la notion d’attribution.

En somme, choisir une licence sous laquelle publier vos données permet à celles et ceux qui vont les utiliser de savoir exactement ce qu’ils peuvent en faire.

### Retirer les informations personnelles et les secrets

Avant de publier vos données sur data.gouv.fr, vérifiez bien que :

* elles ne contiennent pas d’informations qui permettraient d’identifier des individus ;
* elles ne révèlent pas de secret médical, défense, statistique, ou autre secret couvert par la loi.

### Soigner les métadonnées

Les métadonnées sont des données au sujet des données, en l’occurrence il s’agit des données qui servent à décrire votre jeu de données et qui permettent à d’autres personne de le trouver. Voyez ça comme la première de couverture de votre jeu de données, un moyen d’informer rapidement les utilisateurs sur le contenu de votre jeu de données.

[Voir notre article d’aide sur la publication d’un jeu de données](/jeux-de-donnees/publier-un-jeu-de-donnees)

## Et après ?

Une fois votre jeu de données publié, parlez-en autour de vous. Contacter l’équipe en charge de la communication dans votre service, les personnes qui interagissent avec des chercheurs, votre service de relations avec la presse et ainsi de suite. Les données ouvertes n’ont de valeur que si elles sont réutilisées par des tiers.
