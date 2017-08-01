import json

from inspect import isfunction
from pprint import pprint
from jinja2 import contextfilter, contextfunction
from pelican import signals

JINJA_FILTERS = {}
JINJA_GLOBALS = {}


def register_filter(func, name=None, ctx=False):
    name = name or func.__name__
    if ctx:
        func = contextfilter(func)
    JINJA_FILTERS[name] = func


def register_global(func, name=None, ctx=False):
    name = name or func.__name__
    if ctx:
        func = contextfunction(func)
    JINJA_GLOBALS[name] = func


def jinjafilter(name_or_func=None, ctx=False):
    if isfunction(name_or_func):
        register_filter(name_or_func)
        return name_or_func
    else:
        def wrapper(func):
            register_filter(func, name_or_func, ctx)
            return func
        return wrapper


def jinjaglobal(name_or_func=None, ctx=False):
    if isfunction(name_or_func):
        register_global(name_or_func)
        return name_or_func
    else:
        def wrapper(func):
            register_global(func, name_or_func, ctx)
            return func
        return wrapper


@jinjafilter
def prev_page(current, pages):
    prev_page = None
    for page in sorted(pages, key=lambda p: p.date):
        if page == current:
            break
        prev_page = page
    return prev_page


@jinjafilter
def next_page(current, pages):
    found = False
    for page in sorted(pages, key=lambda p: p.date):
        if found:
            return page
        if page == current:
            found = True


@jinjafilter('json')
def json_filter(value):
    return json.dumps(value)


@jinjafilter
def linebreaks(value):
    if isinstance(value, str):
        return value.replace('\n', '<br/>')
    return value


def get_page_from_slug(ctx, slug):
    lang = ctx['DEFAULT_LANG']
    for page in ctx['pages'] + ctx['hidden_pages']:
        if page.slug == slug and page.lang == lang:
            return page


@jinjaglobal(ctx=True)
def page_for(ctx, slug):
    return get_page_from_slug(ctx, slug)


@jinjaglobal(ctx=True)
def children_of(ctx, page_or_slug):
    '''Fetch children pages of a given page'''
    slug = page_or_slug if isinstance(page_or_slug, str) else page_or_slug.slug
    pages = ctx['pages']
    return [p for p in pages if getattr(p, 'parent', None) == slug]


@jinjafilter(ctx=True)
def page_url(ctx, slug):
    page = get_page_from_slug(ctx, slug)
    site_url = ctx['SITEURL']
    if page:
        return '/'.join((site_url, page.url))


@jinjafilter(ctx=True)
def page_title(ctx, slug):
    page = get_page_from_slug(ctx, slug)
    if page:
        return page.title


@jinjaglobal()
def translation_for(obj, lang):
    if hasattr(obj, 'translations'):
        for translation in obj.translations:
            if translation.lang == lang and translation.status not in ('draft', 'hidden'):
                return translation


@jinjafilter
def debug(value, *args):
    print('---- debug value ----')
    pprint(value)
    print('---------------------')
    if args:
        print('---- debug args -----')
        pprint(args)
        print('---------------------')
    return value


def register_jinja_tools(generator):
    generator.env.filters.update(JINJA_FILTERS)
    generator.env.globals.update(JINJA_GLOBALS)


def register():
    signals.generator_init.connect(register_jinja_tools)
