AUTHOR = 'Avez Shariq'
CURRENT_YEAR = 2026
SITENAME = 'Avez Portfolio'
SITEURL = ""

PATH = "content"
THEME = "theme/aubergene"
STATIC_PATHS = ["assets"]
GITHUB_URL = None
DISQUS_SITENAME = None
GOOGLE_ANALYTICS = None

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'code-block',
            'linenums': True,  
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("GitHub", "https://github.com/avezshariq"),
    ("Linkedin", "https://www.linkedin.com/in/avezshariq/")
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
