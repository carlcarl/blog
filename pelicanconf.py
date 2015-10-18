#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'carlcarl'
SITENAME = u'carlcarl\'s blog'
SITEURL = 'http://blog.carlcarl.me'
DISQUS_SITENAME = u'carlcarl'
GITHUB_URL = u'https://github.com/carlcarl'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/carl830'),
          ('github', 'https://github.com/carlcarl'),
          ('facebook', 'http://www.facebook.com/carlcarlking'),
          )
TWITTER_USERNAME = 'carl830'

DEFAULT_PAGINATION = 10

ARTICLE_URL = '{post_id}/{slug}/'
ARTICLE_SAVE_AS = '{post_id}/{slug}/index.html'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
TAG_CLOUD_STEPS = 1
TAG_CLOUD_MAX_ITEMS = 10

import os
# THEME = os.path.expanduser(u'~/Code/pelican-themes/pelican-cait')
THEME = os.path.expanduser(u'~/Code/pelican-cait')

GOOGLE_ANALYTICS = 'UA-24249240-5'

USE_OPEN_GRAPH = True

# MD_EXTENSIONS = ['codehilite','extra']
# MD_EXTENSIONS = ['extra']
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
