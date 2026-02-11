from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_p_5&fp*o6jf=h4h8i8n_$2p@o9@5_#+@ri5u_=j8!a@&@y=bj'
DEBUG = False
ALLOWED_HOSTS = ["tiendamasavi-1.onrender.com"
                 ]
DJANGO_SETTINGS_MODULE = "tiendamasavi.settings"


INSTALLED_APPS = [
    # apps por defecto
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # apps de terceros
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'cloudinary', 
    'cloudinary_storage',

    # mis apps
    "vistaprevia.apps.VistapreviaConfig",

    'registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'tiendamasavi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "template")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # importante para allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tiendamasavi.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===================== STATIC FILES =====================
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_dev")]  # para desarrollo
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")        # para collectstatic en producción
SECRET_KEY = os.environ.get("SECRET_KEY", "031003100310MM0310MmmM")

# ===================== MEDIA FILES ======================
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ===================== AUTH =============================
LOGIN_REDIRECT_URL = '/vistaprevia1'
LOGIN_URL = '/accounts/login/'

# django-allauth settings
SITE_ID = 1
ACCOUNT_ACTIVATION_DAY = 7
REGISTRATION_AUTO_LOGIN = True

# ===================== DEBUG TOOLBAR ====================
"""if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = ["127.0.0.1"]
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}"""

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'imagenesherramientas',
    'API_KEY': '1299031082381293120',
    'API_SECRET': '12381289392108312390213182038102',
}
