# blog.data.gouv.fr

[![CircleCI](https://circleci.com/gh/etalab/blog.data.gouv.fr/tree/master.svg?style=svg)](https://circleci.com/gh/etalab/blog.data.gouv.fr/tree/master)

Pelican blog for Data.gouv.fr

## Getting started

Fork the project, install dependencies and start the live reload web server:

```shell
git clone git@github.com:etalab/blog.data.gouv.fr.git
cd blog.data.gouv.fr
# Create a virtuvalenv or whatever your are used to
pip install -r develop.pip
inv watch
```

You can connect on <http://localhost:5000> to see the website.
Note that drafts will be available at <http://localhost:5000/drafts/>.

## Writing an article

Generate the article markdown file from the template:

```
inv article
```

Edit the markdown file generated in the `article` folder.

### Metadatas

We use Markdown with FrontMatter YAML to handle articles metadata.
Here the list we are using:

- **title**: The article title
- **date**: The creation date
- **modified**: The last modification date
- **image**: An optionnal image used in listings, Atom feeds and when sharing
- **tags**: Some keywords
- **slug**: Key used for multilanguage grouping
- **name**: string used in permalinks
- **lang**: The language used to write the article *(fr|en)*
- **category**: An optionnal category
- **authors**: Who wrote the article
- **summary**: A article summary used in listings, Atom feeds and when sharing
- **status**: Whether the article is published or not *(draft|published)*

### Publishing

Just set the `status` metadata to `published`, commit and push.

The article will be published automatically.

If the article is written in multiple language, set all `status` to `published`


## Adding a page

Generate the page markdown file from the template:

```
inv page
```

Edit the markdown file generated in the `page` folder.


## Working on the theme

The theme is located into the `theme` folder containing

- the templates
- the source assets
- the compiled/minified/optimized assets
- the translations

More details in the README.md from the `theme` directory.


## Documentations

You can fin more documentation on :

- [The Pelican official documentation](http://docs.getpelican.com/)
- [the i18n_subsites README](https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites)
