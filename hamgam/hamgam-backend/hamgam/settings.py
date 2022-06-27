"""
Django settings for hamgam project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os 
import socket

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = Path(BASE_DIR , '/.env')
load_dotenv(env_path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tm(q&qc&g_sp(=^o*v*g)pat^2cc$0wl+s0yk^(^s7)3#))_i8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External 
    "debug_toolbar",
    'rest_framework',
    # CORS
    'corsheaders',
    
    
    # Internal 
    'account.apps.AccountConfig',
    'idea.apps.IdeaConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Debug toolbar  
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # LEAKED PASSWORDS 
    'pwned_passwords_django.middleware.PwnedPasswordsMiddleware',
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]



INTERNAL_IPS = [
    "127.0.0.1",
    
]

ROOT_URLCONF = 'hamgam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hamgam.wsgi.application'

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME':'pwned_passwords_django.validators.PwnedPasswordsValidator',
        'OPTIONS': {'error_message': ('این رمز عبور قبلا هک شده بوده. برای اطلاعات بیشتر /n https://haveibeenpwned.com/ /n  یک سری بزنید')}
    }
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# URL 
ALLOW_UNICODE_SLUGS = True

#### EMIAL STUFF
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


STATIC_URL = '/static/'


 # Cors 

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Account Models
AUTH_USER_MODEL = 'account.Account'


# Logging 

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{BASE_DIR}/../../hamgam/logs/debug.log',
        }

    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

## Coolkie Sessions 


# Rest FrameWork 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'rest_framework.authentication.SessionAuthentication', 
        #'rest_framework.permissons.IsAuthenticatedOrReadOnly',
        ),
}


# Email 

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_email')



# Media 

MEDIA_URL = "/media/"
# any file field upload by default
MEDIA_ROOT =  f"{BASE_DIR}/cdn_test/media"

PROTECTED_MEDIA =  f"{BASE_DIR}/cdn_test/protected"


# Caching Using Redis 
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        #'LOCATION': 'redis://{REDIS_USERNAME}:{REDIS_PASSWORD}@127.0.0.1:6379',
        'LOCATION': 'redis://127.0.0.1:6379',
        'OPTIONS': {
        'db': '0',
        'parser_class': 'redis.connection.PythonParser',
        'pool_class': 'redis.BlockingConnectionPool', 
        }
    },

}

#### NOT ADDING NOW 
## adding uWSGI
# sudo apt-get install uwsgi uwsgi-plugin-python uwsgi-plugin-cgi
