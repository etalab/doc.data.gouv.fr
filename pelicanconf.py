#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import yaml


AUTHOR = 'Etalab'
SITENAME = 'Blog.data.gouv.fr'
SITEURL = ''
GITHUB_URL = 'https://github.com/etalab/blog.data.gouv.fr'

TIMEZONE = 'Europe/Paris'

# All paths are relative to this one
PATH = os.path.dirname(__file__)


def from_yaml(filename):
    with open(os.path.join(PATH, 'data', '{0}.yml'.format(filename))) as data:
        return yaml.load(data)


OUTPUT_PATH = os.path.join(PATH, 'output')

THEME = 'theme'

ARTICLE_PATHS = [
    'articles',
]

PAGE_PATHS = [
    'pages',
]

STATIC_PATHS = [
    'images',
    'circle.yml'  # Ensure no CircleCI build on gh-pages branch
]

PLUGIN_PATHS = [
    'plugins',
]

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TEMPLATE_PAGES = {
    'theme/templates/drafts.html': 'drafts/index.html',
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

SOCIAL_NETWORKS = from_yaml('social')

MENUS = from_yaml('fr/menus')

DEFAULT_PAGINATION = 10

PLUGINS = [
    'sitemap',
    'frontmark',
    'i18n_subsites',
    'related_posts',
    'jinja_tools',
    'tag_cloud',
]

# Jinja Configuration
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n', 'jinja2.ext.with_']
}
I18N_TEMPLATES_LANG = 'en'
I18N_GETTEXT_NEWSTYLE = True

LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
}

# i18n subsites
I18N_SUBSITES = {
    'en': {
        'MENUS': from_yaml('en/menus'),
    },
}


# Pretty URLS
PAGE_URL = '{name}/'
PAGE_SAVE_AS = '{name}/index.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{name}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{name}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

TAGS_URl = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'authors/{slug}/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'

ARCHIVES_URL = 'archvives/'
ARCHIVES_SAVE_AS = 'archvives/index.html'

# Sitemap configuration
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Related posts configuration
RELATED_POSTS_MAX = 3

# Theme config
FAVICON = 'images/favicon.png'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
