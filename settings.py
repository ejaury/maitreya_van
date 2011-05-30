# Django settings for maitreya_van project.
import os, sys
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_DIR, "add_ons"))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: '/home/media/media.lawrence.com/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, "assets")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: 'http://media.lawrence.com', 'http://example.com/media/'
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: 'http://foo.com/media/', '/media/'.
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@+7cb_=v4lmc&$29x^8pg8k&03dj_*terc(j%*xbv3j@3or!sq'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'maitreya_van.urls'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR,"templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.webdesign',
    'django.contrib.admin',
    'south',
    'maitreya_van.pages',
    'maitreya_van.general',
    'maitreya_van.multimedia',
    'maitreya_van.navigation',
    # Third-party
    # ===========
    # django-schedule 1.0 RC-2
    'maitreya_van.schedule',
    'maitreya_van.add_ons.tinymce',
    'photologue',
    'tagging',
    'treemenus',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

# Photologue Settings
PHOTOLOGUE_DIR = 'gallery'
GALLERY_SAMPLE_SIZE = 1
THUMBNAIL_ROW_SIZE = 4

# Schedule Settings
DEFAULT_CALENDAR_SLUG = 'temple'
OCCURRENCE_CANCEL_REDIRECT = '/events/upcoming/calendar/month/temple/'
UPCOMING_EVENTS_LIMIT = 3

# TreeMenu Settings
MAIN_MENU_NAME = 'Main'

# django-tinymce settings
TINYMCE_DEFAULT_CONFIG = {
    'mode': 'textareas',
    'plugins': "searchreplace,table",
    'theme': "advanced",
    'theme_advanced_buttons1_add': "fontsizeselect",
    'theme_advanced_buttons3_add': "search,replace,tablecontrols",
    'theme_advanced_blockformats': 'p,address,pre,h4,h5,h6',
    'convert_fonts_to_spans': 'false',
    'theme_advanced_font_sizes': '80%, 100%, 120%, 135%, 155%, 180%',
    'font_size_style_values': '80%, 100%, 120%, 135%, 155%, 180%',
}

# Authentication
LOGIN_URL = '/admin/login'
LOGIN_REDIRECT_URL = '/admin/'

try:
    import local_settings
except ImportError:
    print """
    -------------------------------------------------------------------------
    You need to create a local_settings.py file which needs to contain at least
    database connection information.

    Copy local_settings.py.example to local_settings.py and edit it.
    -------------------------------------------------------------------------
        """
    import sys
    sys.exit(1)
else:
    # Import any symbols that begin with A-Z. Append to lists any symbols that
    # begin with "EXTRA_".
    import re
    for attr in dir(local_settings):
        match = re.search('^EXTRA_(\w+)', attr)
        if match:
            name = match.group(1)
            value = getattr(local_settings, attr)
            try:
                globals()[name] += value
            except KeyError:
                globals()[name] = value
        elif re.search('^[A-Z]', attr):
            globals()[attr] = getattr(local_settings, attr)
