#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'wradlib'
SITENAME = 'wradlib'
SITEURL = ''#https://wradlib.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
LOCALE = 'C'
#MD_EXTENSIONS = [
#    'codehilite',
#    'extra',
#]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        #'markdown.extensions.headerid': {},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

TYPOGRIFY = True

# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
FILENAME_METADATA = '(?P<slug>.*)'

# Force the same URL structure as WordPress
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_PATHS = ['posts']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['pages']

TEMPLATE_PAGES = {
    'templates/404.html': '404.html',
    #'templates/code.html': 'code/index.html',
    #'templates/themes.html': 'themes/index.html',
}

DIRECT_TEMPLATES = [
    'index', 'tags', 'categories', 'authors', 'archives', 'search']

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Deactivate author URLs
#AUTHOR_SAVE_AS = False
#AUTHORS_SAVE_AS = False

# Feed generation is usually not desired when developing
FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'
FEED_ALL_RSS = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAG_FEED_RSS = 'tag/%s/feed/index.html'
TAG_FEED_ATOM = 'tag/%s/feed/atom/index.html'

# http://example.com/category/categoryname/feed
CATEGORY_FEED_RSS = 'category/%s/feed/index.html'
CATEGORY_FEED_ATOM = 'category/%s/feed/atom/index.html'

FEED_MAX_ITEMS = 5
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'wradlib'
DEFAULT_DATE_FORMAT = '%b. %d, %Y'
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Pagination
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 3

# Theme
THEME = "plumage"

STATIC_PATHS = [
    'uploads',
    'documents',
    'extra',
    'downloads',
]

EXTRA_PATH_METADATA = {
    #'extra/favicon.png': {'path': 'favicon.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

PLUGIN_PATHS = ['plugins-core']
PLUGINS = [
    # Core plugins
    'related_posts',
    'render_math',
    # 'thumbnailer',
    'tipue_search',
    'neighbors',
    'sitemap',
    'gallery',
]

GALLERY_PATH = 'downloads'


### Plugin-specific settings

RELATED_POSTS_MAX = 3

# TODO: align default SITEMAP config to
# http://wordpress.org/extend/plugins/google-sitemap-generator/stats/
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

IMAGE_PATH = "uploads"
THUMBNAIL_DIR = "extra"
THUMBNAIL_SIZES = {
    'thumbnail': '462x?',
}
DEFAULT_TEMPLATE = """<a href="{url}" class="zoomable" title="{filename}">
<img src="{thumbnail}" alt="{filename}"></a>"""


### Theme-specific settings

SITE_THUMBNAIL = SITEURL + '/extra/wradlib_logo.svg.png'
SITE_THUMBNAIL_TEXT = 'WRADLIB'

SITESUBTITLE = "An Open Source Library for Weather Radar Data Processing"

MENUITEMS = (
    ('Home', '/'),
    ('Documentation', 'http://docs.wradlib.org'),
    ('Community', '/community/'),
    ('Downloads', '/downloads/'),
    ('About', '/about/'),
)

TIPUE_SEARCH = True

LEFT_SIDEBAR = """
    <!--<div data-spy="affix" data-offset-top="0">-->
    <!--</div>-->
    """

ARTICLE_EDIT_LINK = 'https://github.com/wradlib/landing-page/edit/master/content/posts/%(slug)s.md'

# Blogroll
LINKS_WIDGET_NAME = "Resources"
LINKS = (('Repository', 'https://github.com/wradlib/wradlib'),
         ('Documentation', 'http://docs.wradlib.org'),
         ('wradlib-user group', 'https://groups.google.com/forum/?fromgroups=#!forum/wradlib-users'),)

# Social widget
SOCIAL_WIDGET_NAME = "Contact"
SOCIAL = (('wradlib', 'mailto:wradlib@wradlib.org'),
          ('Github', 'https://github.com/wradlib'),
          ('Facebook', 'https://www.facebook.com/wradlib/'),)

#COPYRIGHT = """&copy; 2011-2016 wradlib developers"""
DISCLAIMER = "All opinions expressed in this site are own personal opinions of the respective wradlib developers and are not endorsed by, nor do they represent the opinions of their previous, current and future employers or any of its affiliates, partners or customers."


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
