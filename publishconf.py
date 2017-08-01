#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *  # noqa


SITEURL = 'https://blog.data.gouv.fr'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'

DELETE_OUTPUT_DIRECTORY = True

PLUGINS += (  # noqa
    # 'image_optimizer',
    'gzip_cache',
)
