# Django settings for maitreya_van project.
import os, sys
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
WWW_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, '../..'))
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
TIME_ZONE = 'America/Vancouver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: '/home/media/media.lawrence.com/'
MEDIA_ROOT = os.path.join(WWW_ROOT, 'public/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: 'http://media.lawrence.com', 'http://example.com/media/'
MEDIA_URL = '/site_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(WWW_ROOT, 'public/static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: 'http://foo.com/media/', '/media/'.
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'assets'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

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
    'django.contrib.sitemaps',
    'django.contrib.webdesign',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    'south',
    'maitreya_van.authext',
    'maitreya_van.pages',
    'maitreya_van.general',
    'maitreya_van.multimedia',
    'maitreya_van.navigation',
    'maitreya_van.main',
    # Third-party
    # ===========
    'maitreya_van.add_ons.tinymce',
    'captcha',
    'contact_form',
    'photologue',
    'tagging',
    'treemenus',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

# Photologue Settings
PHOTOLOGUE_DIR = 'gallery'
GALLERY_SAMPLE_SIZE = 1
THUMBNAIL_ROW_SIZE = 4
MIN_SLIDESHOW_PHOTOS = 5

# Schedule Settings
DEFAULT_CALENDAR_SLUG = 'temple'
OCCURRENCE_CANCEL_REDIRECT = '/events/'
WIDGET_CONTENT_LIMIT = 3

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

GRAPPELLI_ADMIN_TITLE = 'Providence of Maitreya Buddha Missionary Temple Vancouver'

# Google ReCaptcha
RECAPTCHA_PUBLIC_KEY = '6Ld5HNESAAAAAPcirt1BAbHGT6KTniP5TtpX9KHa'
RECAPTCHA_USE_SSL = True

LOG_FILEPATH = os.path.join(WWW_ROOT, 'logs/web.log')

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


# Define here so we can override LOG_FILEPATH in local_settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(funcName)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file':{
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILEPATH,
            'maxBytes': 1048576, # 1 MB
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'maitreya_van': {
            'handlers': ['file', 'mail_admins'],
            'level': 'INFO',
        }
    }
}
