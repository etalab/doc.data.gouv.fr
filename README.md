# Documentation de data.gouv.fr

Ce dépôt correspond au contenu du site doc.data.gouv.fr...

## Contribuer

**TODO**

## Démarrage rapide

### Ruby natif

Installer bundler

```
gem install bundler
```

Compiler et démarrer un serveur de documentation

```
git clone https://github.com/etalab/doc.data.gouv.fr
cd doc.data.gouv.fr
bundle install
bundle exec jekyll serve
```

La documentation sera disponible sur <a href="http://localhost:4000">http://localhost:4000</a>.

### Docker Compose

Vous pouvez utiliser [docker-compose](https://docs.docker.com/compose/) pour tester vos modifications localement avant de les soumettre.
Pour ce faire, il suffit simplement d'executer la commande:

```
docker-compose up
```

Ceci va télécharger l'image docker de [Jekyll](https://www.jekyll.io/) et installer les dépendances nécéssaires avant d'effectuer le rendu du site.
Le résultat sera disponible sur <http://localhost:4000>. Les modifications sont automatiquement prises en compte et provoquent un nouveau rendu du site.
