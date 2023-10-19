---
title: DCAT
order: 2
---

# Moissonnage DCAT

## DCAT

[DCAT](https://www.w3.org/TR/vocab-dcat/) est une ontologie RDF pour décrire des jeux de données.

L'Europe a publié son extension de DCAT, appelée [DCAT-AP](https://joinup.ec.europa.eu/release/dcat-ap/11).

## Spécificités techniques

Ce moissonneur attend l'URL d'un **catalogue** DCAT (`dcat:Catalog`).

Plusieurs formats sont supportés et découvrables à travers la négociation de contenu :
  - `RDF XML`
  - `JSON-LD`
  - `Turtle`
  - `N3`
  - `NT`
  - `Trig`

La pagination est supportée via l'ontologie [Hydra](https://www.w3.org/community/hydra/wiki/Pagination) (ainsi que l'ancienne version)

## Correspondance des champs du modèle

Par souci de lisibilité, les namespaces suivants sont déclarés :
 - `dcat` ⇨ `http://www.w3.org/ns/dcat#`
 - `dct` ⇨ `http://purl.org/dc/terms/`
 - `foaf` ⇨ `http://xmlns.com/foaf/0.1/`
 - `hydra` ⇨ `http://www.w3.org/ns/hydra/core#`
 - `rdfs` ⇨ `http://www.w3.org/2000/01/rdf-schema#`
 - `scv` ⇨ `http://purl.org/NET/scovo#`
 - `skos` ⇨ `http://www.w3.org/2004/02/skos/core#`
 - `vcard` ⇨ `http://www.w3.org/2006/vcard/ns#`
 - `xsd` ⇨ `http://www.w3.org/2001/XMLSchema#`
 - `freq` ⇨ `http://purl.org/cld/freq/`

### Jeu de données

La notion équivalente au jeu de données sur data.gouv.fr (`Dataset`) est un noeud de type `dcat:Dataset` en RDF.

| | data.gouv.fr | RDF | Notes |
|-|--------------|-----|-------|
| Titre | `title` | `dct:title` | |
| Acronyme | `acronym` | `skos:altLabel` | |
| Description | `description` | `dct:description` + `dct:abstract` | Éventuellement HTML transformé en Markdown. `dct:description` est à privilégier |
| Mots-clés | `tags` | `dcat:keyword` + `dcat:theme` | Les `RdfResource` ne sont pas supportées pour le champ `dcat:theme`. `dcat:keyword` est à privilégier |
| Licence | `license` | `dct:license` et `dct:right` depuis `dcat:distributions` | [Détection des licences]({{ site.baseurl }}{% link _moissonnage/licences.md %}) |
| Couverture spatiale | `spatial` | ❌ | |
| Couverture temporelle | `temporal_coverage` | `dct:temporal` | Séparé par `/` dans le cas de dates de début et de fin, ex: 2011-01-01/2011-12-31 |
| Fréquence de mise à jour | `frequency` | `dct:accrualPeriodicity` | [Dublin Core Frequency](http://dublincore.org/groups/collections/frequency/) ou un équivalent au plus proche des [Fréquences Européennes](https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/frequency) |
{: .table }

#### Autres métadonnées

Certaines propriétés additionnelles sont conservées dans l'attribut `harvest` par soucis de traçabilité.
Les informations de date sont sauvegardées dans ces métadonnées.

| | data.gouv.fr `harvest` | RDF | Notes |
|-|--------------|-----|-------|
| Identifiant distant | `remote_id` | `dct:identifier` | Conservé aussi sous `dct:identifier` |
| URI | `uri` | ID du noeud | `URIRef` |
| URL de consultation | `remote_url` | `dcat:landingPage` ou l'identifier RDF s'il s'agit d'une URI | |
| Date de création | `created_at` | `dct.issued` | |
| Date de modification | `modified_at` | `dct.modified` | |
{: .table }

### Ressource

La notion équivalente à la ressource sur data.gouv.fr (`Resource`) est un noeud de type `dcat:Distribution` en RDF.

| | data.gouv.fr | RDF | Notes |
|-|--------------|-----|-------|
| Titre | `title` | `dct:title` | Propriété facultative, un nom est généré sinon |
| Description | `description` | `dct:description` | Éventuellement HTML transformé en Markdown |
| URL | `url` | `dcat:downloadURL` et `dcat:accessURL`| Priorité à `dcat:downloadURL` |
| Taille | `filesize` | `dcat:bytesSize` ||
| Type MIME | `mime` | `dcat:mediaType` ||
| Format | `format` | `dct:format` ||
| Somme de contrôle | `checksum` | `spdx:checksum` (`spdx:algorithm` + `spdx:checksumValue`) ||
{: .table }

#### Autres métadonnées

Certaines propriétés sont conservées dans l'attribut `harvest` par souci de traçabilité :

| | data.gouv.fr resource `harvest` | RDF | Notes |
|-|--------------------------------|-----|-------|
| Identifiant distant | `dct:identifier` | `dct:identifier` | |
| URI | `uri` | `dct:identifier` | Si `dct:identifier` est un `URIRef` |
| Date de création | `created_at` | `dct.issued` | |
| Date de modification | `modified_at` | `dct.modified` | |
{: .table }

## Logiciels supportés

La plupart des logiciels exposant du DCAT (v1 à date) devraient être compatibles _a minima_ avec le moissonneur DCAT de data.gouv.fr. Ci-dessous quelques exemples de logiciels supportés.

### GeoNetwork

Si vous avez une instance de Geonetwork, vous pouvez publier sur data.gouv.fr.

### GeoNetwork v2 ou v3
En effet, il existe un endpoint DCAT alternatif au endpoint CSW habituellement utilisé comme [documenté sur la doc Geonetwork officielle](https://geonetwork-opensource.org/manuals/3.10.x/en/api/rdf-dcat.html).

Ainsi <https://geosas.fr/geonetwork/srv/fre/csw> deviendra <https://geosas.fr/geonetwork/srv/fre/rdf.search> par exemple.

### GeoNetwork v4

GeoNetwork v4 est maintenant supporté au moissonnage via [CSW avec l'export DCAT](https://github.com/geonetwork/core-geonetwork/wiki/DCAT-enhancements) !
Il faut alors choisir le moissonneur de type `csw-dcat` et configurer l'URL pour pointer vers l'endpoint csw, ex :  <https://geosas.fr/geonetwork/srv/fre/csw>.

Une requête POST est alors effectuée par le moissonneur avec la requête suivant :
```
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2"
                xmlns:gmd="http://www.isotc211.org/2005/gmd"
                service="CSW" version="2.0.2" resultType="results"
                startPosition="1" maxPosition="200"
                outputSchema="http://www.w3.org/ns/dcat#">
      <csw:Query typeNames="gmd:MD_Metadata">
          <csw:ElementSetName>full</csw:ElementSetName>
          <ogc:SortBy xmlns:ogc="http://www.opengis.net/ogc">
              <ogc:SortProperty>
                  <ogc:PropertyName>identifier</ogc:PropertyName>
              <ogc:SortOrder>ASC</ogc:SortOrder>
              </ogc:SortProperty>
          </ogc:SortBy>
      </csw:Query>
  </csw:GetRecords>
```

Attention, si des entrées du catalogue cible ne sont pas convertibles en DCAT, il faut mettre en place un portail dédié en filtrant par exemple sur les entrées de type `documentStandard` pour n'exposer que les entrées compatibles.

### Isogeo

Les portails Isogeo exposent du DCAT et sont donc moissonnables par data.gouv.fr.

Cette [documentation officielle](https://help.isogeo.com/admin/fr/features/publish/harvest_datagouv_fr.html) explique en détail la mise en place d'un moissonneur DCAT pour un portail Isogeo.

## Contribuer

Ce moissonneur fait partie du coeur de `udata`, [son code est disponible sur github](https://github.com/opendatateam/udata/blob/master/udata/harvest/backends/dcat.py). Vous pouvez donc soumettre des améliorations ou signaler des anomalies.
