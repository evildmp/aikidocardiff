# -*- coding: utf-8 -*-
# Django settings for aikidocardiff project.

import os.path

BASE_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = 'daniele@vurt.org'

ADMINS = (
    (u'Daniele Procida', 'daniele@vurt.org'),
)

MANAGERS = ADMINS

from secret_settings import DATABASES

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be avilable on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = BASE_PATH+'/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# The absolute path to the directory where collectstatic will collect static files for deployment.
# Example: "/home/example.com/static/"
STATIC_ROOT = BASE_PATH+'/static/'

# URL to use when referring to static files located in STATIC_ROOT.
# Examples: "/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tr!t%%^11zedj_ljr=*qhohg&amp;p8fkv17mh8u&amp;)l*z#ymg@yd*z'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
#    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
#    )),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    # 'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',

    "cms.context_processors.media",
    'sekizai.context_processors.sekizai',

    "arkestra_utilities.context_processors.arkestra_templates",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'aikidocardiff.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH+'/templates/',
)

INSTALLED_APPS = (

     # Django CMS applications

    'arkestra_utilities',
    'cms',
    'menus',
    # 'appmedia',
    'cms.plugins.text',
    'cms.plugins.snippet',
    'sekizai',
    # 'djcelery',     # will need to be enabled for celery processing

    # Arkestra applications

    'contacts_and_people',
    'vacancies_and_studentships',
    'news_and_events',
    'links',
    'arkestra_utilities.widgets.combobox',
    'arkestra_image_plugin',
    # 'video',
    'housekeeping',

    # other applications

    'polymorphic',
    'semanticeditor',
    'mptt',
    'easy_thumbnails',
    'typogrify',
    'filer',
    'widgetry',
    'south',
    # 'adminsortable',

    # core Django applications
    # these should be last, so we can override their templates

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    )

# ------------------------ Django Celery
try:
    import djcelery
    djcelery.setup_loader()

    BROKER_HOST = "localhost"
    BROKER_PORT = 5672
    BROKER_USER = "guest"
    BROKER_PASSWORD = "guest"
    BROKER_VHOST = "/"
except ImportError:
    pass


# ------------------------ Django Filer

FILER_FILE_MODELS = (
        'video.models.Video',
        'filer.models.imagemodels.Image',
        'filer.models.filemodels.File',
    )

# ------------------------ Django CMS

gettext = lambda s: s

CMS_SOFTROOT = True
CMS_PERMISSION = True
CMS_SEO_FIELDS = True


# this is only here because I don't know how to make other apps find it otherwise, and they rely on it.
CMS_MEDIA_URL = STATIC_URL + 'cms/'

CMS_TEMPLATES = (
    ('aikidocardiff.html', gettext('Aikido Cardiff')),
)

CMS_PAGE_FLAGS = (
    )

CMS_PLACEHOLDER_CONF = {
    'body': {
        "plugins": (
            'SemanticTextPlugin',
            'CMSVacanciesPlugin',
            'CMSNewsAndEventsPlugin',
            'SnippetPlugin',
            'LinksPlugin',
            'CMSPublicationsPlugin',
            'ImagePlugin',
            'ImageSetPublisher',
            'EntityAutoPageLinkPluginPublisher',
            'EntityMembersPluginPublisher',
            'FilerImagePlugin',
            'EntityDirectoryPluginPublisher',
            'CarouselPluginPublisher',
            'FocusOnPluginPublisher',
            'VideoPluginPublisher',
            ),
        "extra_context": {
            "width":"880",
            },
        "name": gettext("body"),
    },
}

LANGUAGES = (
('en', gettext('English')),
('de', gettext('German')),
('cy', gettext('Cymraeg')),
)

# ------------------------ WYMeditor/SemanticEditor

# these override the settings in cms.plugins.text.settings

WYM_TOOLS = ",\n".join([
    "{'name': 'Italic', 'title': 'Emphasis', 'css': 'wym_tools_emphasis'}",
    "{'name': 'Bold', 'title': 'Strong', 'css': 'wym_tools_strong'}",
    "{'name': 'InsertOrderedList', 'title': 'Ordered_List', 'css': 'wym_tools_ordered_list'}",
    "{'name': 'InsertUnorderedList', 'title': 'Unordered_List', 'css': 'wym_tools_unordered_list'}",
    "{'name': 'Indent', 'title': 'Indent', 'css': 'wym_tools_indent'}",
    "{'name': 'Outdent', 'title': 'Outdent', 'css': 'wym_tools_outdent'}",
    "{'name': 'Undo', 'title': 'Undo', 'css': 'wym_tools_undo'}",
    "{'name': 'Redo', 'title': 'Redo', 'css': 'wym_tools_redo'}",
    "{'name': 'ToggleHtml', 'title': 'HTML', 'css': 'wym_tools_html'}",
])

WYM_CONTAINERS = ",\n".join([
    "{'name': 'P', 'title': 'Paragraph', 'css': 'wym_containers_p'}",
   # "{'name': 'H1', 'title': 'Heading_1', 'css': 'wym_containers_h1'}", # I assume you reserve <h1> for your page templates
    "{'name': 'H2', 'title': 'Heading_2', 'css': 'wym_containers_h2'}",
    "{'name': 'H3', 'title': 'Heading_3', 'css': 'wym_containers_h3'}",
    "{'name': 'H4', 'title': 'Heading_4', 'css': 'wym_containers_h4'}",
    "{'name': 'H5', 'title': 'Heading_5', 'css': 'wym_containers_h5'}",
    "{'name': 'H6', 'title': 'Heading_6', 'css': 'wym_containers_h6'}",
#    "{'name': 'PRE', 'title': 'Preformatted', 'css': 'wym_containers_pre'}",
   "{'name': 'BLOCKQUOTE', 'title': 'Blockquote', 'css': 'wym_containers_blockquote'}",
   # "{'name': 'TH', 'title': 'Table_Header', 'css': 'wym_containers_th'}", # not ready for this yet
])

from arkestra_settings import *

# Override the server-derived value of SCRIPT_NAME
# See http://code.djangoproject.com/wiki/BackwardsIncompatibleChanges#lighttpdfastcgiandothers
FORCE_SCRIPT_NAME = ''
