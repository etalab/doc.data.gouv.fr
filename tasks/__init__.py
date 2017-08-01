import logging
import os
import shutil
import slugify
import sys

from datetime import datetime

from invoke import run as raw_run, task

from pelican import Pelican, log

from pelican.settings import read_settings
from jinja2 import Environment, FileSystemLoader

try:
    from importlib import reload
except:
    from imp import reload


#: Project absolute root path
TASKS_ROOT = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(TASKS_ROOT, '..'))

CONF_FILE = os.path.join(ROOT, 'pelicanconf.py')

# Port for `serve`
PORT = 5000

THEME_DIR = os.path.join(ROOT, 'theme')
TRANSLATIONS_DIR = os.path.join(THEME_DIR, 'translations')
TRANSLATIONS = ['fr']
LANGUAGES = ['en'] + TRANSLATIONS


class objdict(dict):
    def __getattr__(self, name):
        return self[name]


def get_settings():
    return objdict(read_settings(CONF_FILE))


jinja_env = Environment(loader=FileSystemLoader(TASKS_ROOT))


def jinja(template, filename, **ctx):
    template = jinja_env.get_template(template)
    with open(filename, 'wb') as out:
        data = template.render(**ctx)
        out.write(data.encode('utf-8'))


def run(cmd, *args, **kwargs):
    '''Run a command ensuring cwd is project root'''
    return raw_run('cd {0} && {1}'.format(ROOT, cmd), *args, **kwargs)


@task
def clean(ctx):
    '''Remove generated files'''
    settings = get_settings()
    if os.path.isdir(settings.OUTPUT_PATH):
        shutil.rmtree(settings.OUTPUT_PATH)
        os.makedirs(settings.OUTPUT_PATH)


@task
def publish(ctx):
    '''Publish on githubpages'''
    run('ghp-import -p output')


def draft(article=False):
    '''Create a draft page'''
    title = input('Title: ')
    slug = slugify.slugify(title, to_lower=True)
    name = slugify.slugify(title, to_lower=True)
    slug = input('Slug ({0}): '.format(slug)) or slug
    name = input('Name ({0}): '.format(name)) or name
    lang = input('Language ({0}): '.format('fr')) or 'fr'
    summary = input('Summary: ')
    tags = [t for t in input('Tags: ').split(',') if t]
    category = input('Category: ') if article else None
    now = datetime.now()
    if article:
        filename = '{0}-{1}.md'.format(now.date().isoformat(), slug)
        filename = os.path.join('articles', lang, filename)
    else:
        filename = os.path.join('pages', lang, '{0}.md'.format(slug))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    jinja('draft.j2.md', filename,
          title=title,
          slug=slug,
          name=name,
          category=category,
          summary=summary,
          tags=tags,
          lang=lang,
          is_article=article,
          date=now)


@task
def page(ctx):
    '''Create a draft page'''
    draft(article=False)


@task
def article(ctx):
    '''Create a draft article'''
    draft(article=True)


@task
def i18n(ctx):
    '''Extract theme translatable strings'''
    run('cd {0} && pybabel extract -F babel.cfg -o {1}/messages.pot .'.format(
        THEME_DIR, TRANSLATIONS_DIR
    ))
    for lang in TRANSLATIONS:
        pofile = os.path.join(TRANSLATIONS_DIR, lang, 'LC_MESSAGES/messages.po')
        if os.path.exists(pofile):
            run('pybabel update -i {0}/messages.pot -d {0} -l {1}'.format(TRANSLATIONS_DIR, lang))
        else:
            run('pybabel init -i {0}/messages.pot -d {0} -l {1}'.format(TRANSLATIONS_DIR, lang))


@task
def i18nc(ctx):
    '''Compile theme translations'''
    run('pybabel compile -d {0}'.format(TRANSLATIONS_DIR))


@task(i18nc)
def build(ctx, verbose=False, debug=False):
    '''Build local version of site'''
    cmd = 'pelican -s publishconf.py'
    if verbose:
        cmd += ' -v'
    if verbose:
        cmd += ' -D'
    run(cmd)


def reload_and_compile():
    _sys_path = sys.path[:]
    settings = get_settings()
    for pluginpath in settings.PLUGIN_PATHS:
        sys.path.insert(0, pluginpath)
    for name, module in sys.modules.items():
        root_module = name.split('.', 1)[0]
        if root_module in settings.PLUGINS:
            reload(module)

    sys.path = _sys_path
    compile()


def compile():
    settings = get_settings()
    p = Pelican(settings)
    try:
        p.run()
    except SystemExit as e:
        pass


@task(i18nc)
def watch(ctx, verbose=False):
    '''Serve the blog and watch changes'''
    from livereload import Server

    settings = get_settings()

    log.init(logging.DEBUG if verbose else logging.INFO)
    logging.getLogger('livereload').propagate = False
    logging.getLogger('tornado').propagate = False

    compile()
    server = Server()
    server.watch(CONF_FILE, compile)

    server.watch('theme/static', compile)
    server.watch('theme/templates', compile)
    server.watch('theme/translations', compile)
    server.watch('data', compile)
    server.watch('plugins', reload_and_compile)

    paths = settings.ARTICLE_PATHS + settings.PAGE_PATHS
    for path in paths:
        server.watch(path, compile)

    server.serve(port=PORT, root=settings.OUTPUT_PATH)
