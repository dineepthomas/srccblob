#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'srcc members'
SITENAME = 'SRCC blog'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('SRCC Home', 'https://www.srcc.lsu.edu/'),
         ('SRCC"s CLIMATE EXTREMES PORTAL', 'http://extremes.srcc.lsu.edu/'),
         ('Climdat', 'https://climdata.srcc.lsu.edu/'),
        )

# Feeds 
FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),
          ('OPW', 'feeds/tag/opw.atom.xml'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/srcclsu'),
          ('Facebook', 'https://www.facebook.com/srcclsu'),)

# Static path
STATIC_PATHS= ['images']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first

NEWEST_FIRST_ARCHIVES = False

# Specify theme

THEME = "bootstrap2"

DISQUS_SITENAME = 'blog.srcc.lsu.edu'

HEADER_COVER = 'images/srcclogo.png'
MENUITEMS = [['Posts', SITEURL]]