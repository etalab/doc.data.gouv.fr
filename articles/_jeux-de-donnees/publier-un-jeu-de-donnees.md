---
title: Publier un jeu de données
slug: publier-un-jeu-de-donnees
redirect_from: /jeux-de-donnees/publier-un-jeu-de-donnes/
---
# 💡 Une nouvelle documentation est disponible ! 

[Découvrez la nouvelle version beta des guides et de la documentation de data.gouv.fr](https://guides.data.gouv.fr/publier-des-donnees/guide-data.gouv.fr/jeux-de-donnees/publier-un-jeu-de-donnees)

# Publier un jeu de données

La publication d’un jeu de données sur data.gouv.fr nécessite la création d’un compte gratuit.

Pour mettre en ligne un nouveau jeu de données :

1. [Connectez-vous à votre compte](https://www.data.gouv.fr/fr/login) ;
2. Rendez-vous sur [la page de création d’un jeu de données](https://www.data.gouv.fr/fr/admin/dataset/new/), en cliquant sur le bouton **Publiez un jeu de données** dans le bandeau **Participez** en bas de page.

À partir de là, la publication se déroule en 4 étapes.

## 1. Définir qui publie les données

Sur data.gouv.fr, vous pouvez mettre en ligne des jeux de données :

- sous votre propre nom, à titre individuel ;
- pour le compte d’une organisation, à titre collectif.

L’étape 1 de la publication d’un jeu de données vous permet de choisir si les données doivent être publiées à votre nom ou sous la bannière de votre organisation. Si vous êtes membre d’une organisation, nous vous conseillons de publier vos jeux de données en son nom, lorsque cela vous semble pertinent, dans le but d’éviter l’éparpillement de vos publications.

## 2. Décrire votre jeu de données

L’étape 2 de la publication d’un jeu de données vous permet de décrire les données que vous publiez. Cette étape est cruciale pour que vos données soient bien référencées et facile à réutiliser.

### Titre

La plupart des utilisateurs de data.gouv.fr trouvent des jeux de données grâce à un moteur de recherche. Afin que vos données soient faciles à trouver, employez le même vocabulaire que le public pour les décrire. Cela commence par un titre spécifique et précis, car le titre est l’élément qui a le plus d’importance aux yeux des moteurs de recherche.

- **Mauvais titre** : Horaires des cars
- **Bon titre** : Horaires des autobus de la ville de Brive pour la période 2018 – 2019

La présence d’un titre est obligatoire.

### Sigle

Vous pouvez associer un sigle à votre jeu de données. Par exemple, à la [base des entreprises et de leurs établissements](https://www.data.gouv.fr/fr/datasets/5862206588ee38254d3f4e5e), produite par l’INSEE, est associé le sigle SIRENE. Les lettres qui composent votre sigle n’ont pas besoin d’être séparées par des points.

- **Mauvais sigle** : I.R.V.E.
- **Bon sigle** : IRVE

La présence d’un sigle est facultative.

### Description

Chaque jeu de données publié sur data.gouv.fr doit être accompagné d’une description. Cette dernière permet aux personnes qui consultent votre jeu de données de comprendre, en quelques lignes, ce qu’il est possible de faire avec vos données, pourquoi elles sont utiles, et comment les manipuler. La description est importante, car c’est généralement la première chose que les gens lisent quand ils découvrent vos données.

Les descriptions répondent généralement aux questions suivantes :

- Que contient le jeu de données ? Combien y a-t-il de fichiers ?
- Comment les données sont-elles structurées ? À quoi correspondent les colonnes des fichiers CSV ou les tables de la base ?
- À quoi sert le jeu de données ? Quelle est sa raison d’être ?
- Qui est à l’origine du jeu de données ? Qui le tient à jour ?
- Comment lire le jeu de données ? Comment ouvrir les fichiers ?
- Comment contacter le producteur des données ? À qui s’adresser en cas de problème ?

Répondre à ces questions dans votre description permet aux utilisateurs de récupérer et manipuler vos données facilement.

La [syntaxe Markdown](https://fr.wikipedia.org/wiki/Markdown) est prise en charge dans le champ de saisie de la description. Elle vous permet de mettre en forme le texte de votre description, pour y ajouter des titres, des sous-titres, des listes à puces, du gras, ou encore des liens vers d’autres pages web.

La présence d’une description est obligatoire.

### Licence

Nous vous conseillons de choisir une licence sous laquelle publier vos données, mais rien ne vous y oblige. Si vos données sont ouvertes, nous vous recommandons [la licence ouverte](https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf) ; si elle contiennent une obligation de réciprocité, [la licence oDbL](https://spdx.org/licenses/ODbL-1.0.html#licenseText) convient bien. En choisissant une licence, vous permettez au public de savoir s’il peut adapter et réutiliser vos données et sous quelles conditions. Si vous ne choisissez pas de licence, vos données sont alors soumises au cadre légal définit dans le [Code des relations entre le public et l’administration](https://www.legifrance.gouv.fr/affichCode.do;jsessionid=E4583EBE2857A0DF9056D5D0082F8F2D.tplgfr31s_2?idSectionTA=LEGISCTA000032255212&cidTexte=LEGITEXT000031366350&dateTexte=20181016).

La présence d’une licence est facultative.

[Voir comment bien choisir une licence](https://www.data.gouv.fr/fr/licences)

### Fréquence de mise à jour

Vous devez définir une fréquence _théorique_ de mise à jour pour votre jeu de données. Il s’agit de la fréquence à laquelle vous prévoyez de vous reconnecter sur data.gouv.fr pour mettre à vos données. Cette fréquence est indicative.

La fréquence de mise à jour est obligatoire. La date de dernière mise à jour des données est facultative.

### Mots clefs

Vous pouvez ajouter des mots clefs à votre jeu de données. Les mots clefs peuvent indiquer votre secteur d’activité (par exemple `agriculture`), votre type de structure (par exemple `ministère`), ou encore votre sujet (par exemple `élevage`). Les mots clefs apparaissent sur la page de présentation de votre jeu de données. Vous pouvez cliquer sur un mots clef pour voir la liste des autres jeux de données auquel le mot clef en question a été assigné. Dit autrement, c’est un moyen de découvrir de nouveaux jeux de données.

Les mots clefs sont facultatifs.

### Couverture temporelle

Vous avez la possibilité de préciser la période couverte par vos données, c’est-à-dire les dates qu’elles concernent. Par exemple, si vous publiez un calendrier, utilisez ce champ pour préciser les années couvertes par votre calendrier.

La couverture temporelle est facultative.

### Couverture spatiale

La couverture spatiale de vos données correspond aux zones géographiques qu’elles couvrent et pour lesquelles elles sont pertinentes. Si vos données concernent une ville ou un pays en particulier, c’est ici que vous précisez le nom de la ville ou celui du pays en question. Si vos données concernent plusieurs zones géographiques, vous pouvez les ajouter les unes à la suite des autres, comme s’il s’agissait de mots clefs.

La couverture spatiale est facultative.

### Granularité spatiale

La granularité spatiale complète la couverture spatiale. Si la couverture spatiale fixe le cadre de la zone géographique couverte par les données, la granularité spatiale décrit le niveau de zoom auquel il est possible de descendre à l’intérieur des données en question. Dit autrement, il s’agit du niveau de finesse de vos données, du plus petit dénominateur qu’elles contiennent.

Par exemple, si vous avez un fichier CSV qui contient les coordonnées géographiques de tous les gymnases du territoire français, alors :

- votre couverture spatiale correspond à la France, car vos données couvrent l’ensemble du territoire ;
- votre granularité spatiale se situe au niveau du point d’intérêt (le gymnase étant ici considéré comme un point d’intérêt).

La granularité spatiale est facultative.

### Privé

Si vous souhaitez créer un jeu de données, mais que vous ne souhaitez pas le mettre en ligne tout de suite, vous pouvez cocher la case **Privé**. Quand votre jeu de données est prêt pour le grand soir, décochez la case.

Une fois l’étape 2 complétée, cliquez sur le bouton **Suivant**, présent en bas à droite de la page, pour passer à la dernière étape de la publication : celle de l’importation de vos fichiers.

## 3. Importer vos fichiers

Une fois votre jeu de données décrit, vient le temps d’importer les fichiers ou ressources qui le composent. Pour importer votre premier fichier, cliquez sur le bouton **Choisissez un fichier de votre ordinateur**. Une fois votre fichier importé, vous pouvez le décrire en complétant le formulaire qui apparaît alors sur votre écran. Si votre jeu de données contient plusieurs fichiers, remplissez un formulaire par fichier.

### Titre

Le titre de votre fichier doit être descriptif. Par défaut, nous reprenons le titre qu’avait votre fichier au moment de l’importation, mais rien ne vous empêche de le modifier à cette étape si vous souhaitez le préciser.

Si vous référencez un fichier hébergé ailleurs que sur data.gouv.fr, ce champ correspond au nom donné à votre fichier lors de sa mise en ligne.

Le titre est obligatoire.

### Type

Pour chaque fichier importé sur data.gouv.fr, vous devez choisir une catégorie dans laquelle le ranger, parmi :

- **fichier principal** : désigne tous les fichiers qui contiennent vos données brutes ;
- **documentation** : désigne les fichiers annexes, qui contiennent généralement des explications au sujet de vos fichiers principaux ;
- **mise à jour** : permet d’indiquer que le fichier importé met à jour un _fichier principal_ précédement mis en ligne ;
- **API** : désigne l’API qui permet d’accéder à vos données et vers laquelle vous ajoutez un lien dans le champ **URL** qui se trouve plus bas ;
- **dépôt de code** : désigne le dépôt de code (_repository_ en anglais) qui contient vos données et vers lequel vous ajoutez un lien dans le champ **URL** qui se trouve plus bas ;
- **autre** : pour tous les autres types de fichier.

La désignation du type de fichier est obligatoire.

### Description

Vous pouvez décrire votre fichier pour indiquer ce qu’il contient. La description prend en compte la syntaxe Markdown.

La description est facultative, mais conseillée.

### Date de publication

Par défaut, il s’agit de la date à laquelle vous importez votre fichier sur data.gouv.fr, mais vous êtes libre de la changer.

Si vous référencez un fichier hébergé ailleurs que sur data.gouv.fr, il s’agit de la date à laquelle votre fichier a été mis en ligne.

La date de publication est facultative.

### Schéma

Les schémas de données permettent de décrire des modèles de données : quels sont les différents champs, comment sont représentées les données, quelles sont les valeurs possibles etc.
Pour en savoir plus sur les schémas, consultez [schema.data.gouv.fr](https://schema.data.gouv.fr/).

Il s'agit pour ce champ de l’identifiant du schéma auquel la ressource adhère, le cas échéant.

Deux cas possibles :
- si vous importez un fichier, une validation sera effectuée sur la ressource pour s’assurer qu’elle correspond bien au fichier indiqué.
- si vous référencez un fichier hébergé ailleurs, sur un autre site, aucune validation de correspondance au schéma n’est effectuée.

Le schéma est facultatif.

### URL

Deux cas possibles :

- si vous importez un fichier, vous ne pouvez pas modifier ce champ, car il s’agit alors de l’URL assignée par data.gouv.fr à votre ressource ;
- si vous référencez un fichier hébergé ailleurs, sur un autre site, ajoutez ici l’URL canonique (qui ne varie pas) permettant d’accéder directement au fichier en question.

L’URL est obligatoire.

### Taille

Là encore, deux cas à distinguer :

- si vous importez votre fichier, vous n’avez rien à faire, car nous calculons la taille de votre ressource pour vous ;
- si vous référencez un fichier hébergé ailleurs, indiquez ici sa taille (en octets).

La taille est facultative.

### Format

Le format du fichier que vous ajoutez. Deux possibilités :

- si vous importez votre fichier, nous détectons automatiquement son format, vous n’avez donc rien à faire ;
- si vous référencez un fichier externe, précisez ici son format.

Le format est obligatoire.

### Type MIME

Le type MIME est un [identifiant de format de données](https://fr.wikipedia.org/wiki/Type_de_médias) à la syntaxe assez stricte.

Là encore :

- si vous importez votre fichier, votre type MIME est pré-rempli, vous n’avez donc rien à faire ;
- si vous référencez un fichier externe, sélectionnez le type MIME qui s’y rapporte parmi [la liste des types MIME](https://fr.wikipedia.org/wiki/Type_de_médias).

Le type MIME est facultatif.

### Somme de contrôle

La somme de contrôle permet de calculer l’empreinte d’un fichier, pour s’assurer que ce dernier ne varie pas au gré des copies, transferts, ou restaurations.

Deux cas doivent ici être distingués :

- si vous importez votre fichier, vous n’avez rien à faire, car la somme de contrôle est créée par data.gouv.fr ;
- si vous référencez un fichier externe, vous pouvez indiquer ici votre propre somme de contrôle. Le menu déroulant permet de sélectionner l’algorithme utilisé pour créer la somme de contrôle, parmi : `sha1`, `sha2`, `sha256`, `md5`, `crc` (nous vous conseillons d’utiliser `sha256`si vous en avez la possibilité).

La somme de contrôle est facultative.

Une fois votre fichier décrit, cliquez sur le bouton **Suivant** qui se trouve en bas à droite de la page pour l’importer et publier votre jeu de données.

## 4. Voir et compléter un jeu de données existant

Une fois votre première ressource publiée, votre jeu de données devient accessible en ligne, vous pouvez alors :

- voir votre jeu de données sur data.gouv.fr en cliquant sur le bouton **Voir sur le site** ;
- ajouter d’autres ressources à votre jeu de données en cliquant sur le bouton **Voir dans l’administration** ;
- partager votre jeu de données sur les réseaux sociaux en cliquant sur l’icône associée au réseau social qui vous concerne.

### Ajouter d’autres ressources à un jeu de données existant

Pour ajouter des ressources supplémentaires à un jeu de données déjà en ligne, cliquez sur le nom du jeu de données que vous souhaitez enrichir quand vous vous situez [sur la page Moi](https://www.data.gouv.fr/fr/admin/me/).

Une fois sur la page du jeu de données à modifier :

1. Naviguez jusqu’au bloc intitulé **Ressources** ;
2. Cliquez sur le bouton **Ajouter** ;
3. Cliquez sur le bouton **Choisissez un fichier de votre ordinateur** ;
4. Complétez les informations associées à votre ressources, comme vous l’avez fait à l’étape 3 de la création de votre jeu de données ;
5. Cliquez sur le bouton **Enregistrer**.

Refaites la procédure ci-dessus autant de fois que vous souhaitez ajouter de ressources à votre jeu de données.
