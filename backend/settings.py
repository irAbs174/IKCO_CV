from .locals import *
from .apps import *
from pathlib import Path
import os
from django_storage_url import dsn_configured_storage_class


BASE_DIR = Path(__file__).resolve().parent.parent

X_FRAME_OPTIONS = 'SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'cms.context_processors.cms_settings',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',

                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',

            ],
        },
    },
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMS_TEMPLATES = [
    ('index/index.html', 'Home'),
    ('products/single.html', 'product_single'),
    ('products/archive.html', 'product_archive'),
    ('blog/single.html', 'blog_single'),
    ('blog/archive.html', 'blog_archive'),
    ('accounts/login/login.html', 'login'),
    ('blog/archive.html', 'blog_archive'),
    ('utils/factor/factor.html', 'Minimal template'),
    ('minimal.html', 'Minimal template'),
    ('bootstrap5.html', 'Bootstrap 5 Demo'),
    ('whitenoise-static-files-demo.html', 'Static File Demo'),
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite://:memory:')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'core.MD',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

LANGUAGE_CODE = 'fa'

LANGUAGES = [
    ('fa', 'Persian'),
    ('en', 'English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_collected')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_STORAGE_DSN = os.environ.get('DEFAULT_STORAGE_DSN')

DefaultStorageClass = dsn_configured_storage_class('DEFAULT_STORAGE_DSN')

DEFAULT_FILE_STORAGE = 'backend.settings.DefaultStorageClass'

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join('/data/media/')

SITE_ID = 1