---
title: Que publier et comment le publier
slug: que-publier-et-comment-le-publier
---

# Que publier sur data.gouv.fr et comment le publier

data.gouv.fr est la plateforme ouverte des données publiques française. En ce sens, elle met en relation des producteurs et des utilisateurs de données. Une donnée est considérée comme ouverte quand elle peut être consultée, utilisée, et partagée par tous.

## Qui peut publier

Tout le monde peut publier des données sur data.gouv.fr, du moment qu’il s’agit de données d’intérêt public.

Plus précisément, vous pouvez publier des données sur data.gouv.fr :

- Si vous produisez ou collectez des données dans le cadre d’une mission de service public, à condition que ces données ne contiennent pas d’informations personnelles et qu’elles ne révèlent pas de secrets.
- Si vous enrichissez ou complétez des données publiques pour le compte d’une association, d’un projet de recherche, ou sur votre temps libre.
- Si vous produisez des données d’intérêt public de votre côté, même hors du cadre d’une mission de service public.

## Que publier

Nous vous conseillons de publier des données, c’est-à-dire des informations structurées, facilement lisibles par une machine.

Plus concrètement, un fichier Word qui contient des informations sur un projet d’urbanisme ne peut pas être considéré comme une donnée, c’est une information, un document administratif. En revanche, la liste des projets d’urbanisme à l’échelle d’une collectivité peut constituer un jeu de données, surtout si les projets sont rangés dans des colonnes avec une ligne par projet, pour chaque projet.

Si vous ne savez pas par où commencer, voici quelques idées de jeux de données à publier :

- la liste des délibérations adoptées par une assemblée locale — [voir un exemple](https://www.data.gouv.fr/fr/datasets/5a8f387988ee381bb2a62a46) ;
- la liste des subventions attribuées par une collectivité — [voir un exemple](https://www.data.gouv.fr/fr/datasets/5bd8fb5706e3e72ba58c0ec2) ;
- la liste des équipements publics gérés par une collectivité — [voir un exemple](https://www.data.gouv.fr/fr/datasets/595c271ca3a7296408d69b92) ;
- la liste annuelle des prénoms des nouveaux-nés déclarés à l’état-civil — [voir un exemple](https://www.data.gouv.fr/fr/datasets/5407f862a3a7292ef9c20a61).

## Comment le publier

### Choisir un format de publication standardisé

Les données publiées sur data.gouv.fr ont vocation à être consultées et utilisées par d’autres personnes. Pour que tout le monde puisse lire vos données, nous vous encourageons à les publier dans un format ouvert, standard, et non-propriétaire.

Les formats ouverts (CSV par exemple) sont pareils aux moteurs des vieilles voitures, dans le sens où un bon mécanicien peut y mettre les mains et facilement accéder à toutes les pièces qui composent le moteur : rien n’est verrouillé, tout est démontable. Par opposition, les formats propriétaires (XLS par exemple) ressemblent aux moteurs des voitures modernes, dans lesquels toutes les pièces sont cachées dans une boîte, elle même scellée, de sorte que seul un réparateur agréé peut intervenir sur le moteur.

Pour chaque grand type de données, il existe un ou plusieurs format standard, communément accepté et recconu par les gens du métier. En voici un bref aperçu.

#### Données tabulaires

Les données tabulaires (feuilles de calcul), gagnent à être publiées sous la forme de fichiers CSV (_comma-separated values_), reconnaissables à leur extension en `.csv`. Si le fichier que vous avez entre les mains est un fichier Excel, nous vous conseillons d’exporter vos données au format CSV. [Voir comment exporter des données au format CSV à partir d’Excel](https://www.ibm.com/support/knowledgecenter/fr/SSWU4L/WebLanding/imc_WebLanding/WebLanding_q_a_watson_assistant/Saving_a_CSV_file_with_UTF-8_encoding.html). Pourquoi du CSV et pas du XLS comme tout le monde ? Justement car tout le monde n’utilise pas Excel, qui est un logiciel payant.

Quand vous créez votre fichier CSV, nous vous conseillons de :

- inclure les noms des colonnes sur votre première, en les séparant par des virgules ;
- séparer chacune de vos valeurs par une virgule, comme s’il s’agissait de colonnes ;
- encoder votre fichier en UTF-8 (Unicode) pour garantir un bon encodage des caractères accentués.

#### Données de transport

Nous conseillons les formats suivants pour la publication des données de transport :

- GTFS ;
- NeTEx.

[Voir la documentation de transport.data.gouv.fr](https://transport.data.gouv.fr/guide)

#### Données géographiques

Nous conseillons les formats suivants pour la publication des données géographiques :

- GeoJSON, Shapefile, MapInfo MIF/MID, MapInfo TAB et GML, pour les vecteurs ;
- ECW, JPEG2000 et GeoTIFF, pour les données pixelisées (raster).

[Voir la documentation de geo.data.gouv.fr](https://geo.data.gouv.fr/fr/doc/publish-your-data)

#### Données hiérarchiques

Si vos données comportent une structure interne, alors nous vous recommandons les formats suivants :

- JSON ;
- XML ;
- YAML.

#### Images, vidéos et son

Les images, les vidéos, et les sons ne constituent pas des jeux de données à part entière, il s’agit de simples documents, des fichiers statiques. Par conséquent, nous vous déconseillons d’importer des images, des vidéos, ou des sons sur data.gouv.fr, sauf rares exceptions.

En revanche, une _liste_ de photographies peut être considérée comme un jeu de données, à condition que cette liste prenne la forme d’un CSV, dans lequel chaque ligne contient des informations sur chaque photographie : lieu de la prise de vue, date, URL du fichier, auteur du cliché, et ainsi de suite…

#### Documents bureautiques

Même raisonnement que pour les images et les vidéos : les fichiers Word, PowerPoint, ou PDF, ne constituent pas nécessairement des jeux de données, par conséquent leur importation sur data.gouv.fr est déconseillée. Cela dit, une liste de fichiers PDF peut constituer un jeu de données, surtout si la liste est accompagnée d’un CSV qui contient des informations supplémentaires sur chaque PDF.

#### Autres types de données

Pour approfondir la question des formats, nous vous conseillons de jeter un œil au [référentiel général d’interopérabilité](https://references.modernisation.gouv.fr/interoperabilite) (disponible au format PDF), qui référence les normes et les standards au sein des systèmes d’information de l’administration.

### Choisir une licence

Nous vous conseillons de publier vos données sous une licence ouverte :

- si vous êtes une administration, pour simplifier le travail des réutilisateurs ;
- si vous êtes un particulier, pour que vos données puissent être réutilisées par d’autres personnes.

Etalab recommande la [Licence Ouverte](https://github.com/etalab/licence-ouverte/blob/master/LO.md).

#### Quand la publication est faite par une administration

Par défaut, les données publiées sur data.gouv.fr _par des administrations_ tombent sous le coup du [Code des relations entre le public et l'administration](https://www.legifrance.gouv.fr/affichCode.do;jsessionid=E4583EBE2857A0DF9056D5D0082F8F2D.tplgfr31s_2?idSectionTA=LEGISCTA000032255212&cidTexte=LEGITEXT000031366350&dateTexte=20181016), qui stipule notamment que :

> Les informations publiques figurant dans des documents communiqués ou publiés par les administrations (…) peuvent être utilisées par toute personne qui le souhaite à d'autres fins que celles de la mission de service public pour les besoins de laquelle les documents ont été produits ou reçus.

Si tout est déjà écrit dans le Code des relations entre le public et l’administration, pourquoi choisir une licence au moment de la publication des données alors ? Pour faire simple. Les licences permettent à d’autres personnes de savoir ce qu’il est permis de faire avec vos données, sans pour autant devoir lire l’intégralité du Code des relations entre le public et l'administration.

#### Quand la publication est faite par un particulier

Quand un particulier publie des données sur <https://www.data.gouv.fr>, les données mises en lignes sont soumises au droit commun, c’est-à-dire au code de la propriété intellectuelle. Le particulier a l’origine de la publication détient alors la propriété intellectuelle des données. Mais comment donner à d’autres le droit d’utiliser les données en question ? C‘est là qu’interviennent les licences.

Choisir une licence, c’est permettre à d’autres personnes d’utiliser et de modifier des données, sans pour autant en perdre la propriété intellectuelle. Dit autrement, sans licence, les données publiées sur <https://www.data.gouv.fr> par un particulier ne peuvent pas être réutilisées par d’autres personnes, car elles ne tombent pas par défaut sous le coup de la loi CADA.

### Retirer les informations personnelles et les secrets

Avant de publier vos données sur data.gouv.fr, vérifiez bien que :

- elles ne contiennent pas d’informations qui permettraient d’identifier des individus ;
- elles ne révèlent pas de secret médical, défense, statistique, ou [autre secret couvert par la loi](https://www.cada.fr/particulier/les-secrets-proteges-par-la-loi).

### Soigner les métadonnées

Les métadonnées sont des informations qui décrivent vos données. Elles sont prises en compte par le moteur de recherche de data.gouv.fr, ce qui permet à d’autres personnes de les trouver facilement.

[Voir notre article d’aide sur la publication d’un jeu de données](/jeux-de-donnees/publier-un-jeu-de-donnees)

## Et après ?

Une fois votre jeu de données publié, gardez un œil sur la page qui y est associé sur data.gouv.fr, pour surveiller les discussions. Répondez aux questions qui vous sont posées. Vous verrez peut-être aussi d’autres personnes publier des réutilisations réalisées à partir de vos données.
