"""
Django settings for fgf project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
#from dj_rest_authallauth import *
#import dj_database_url

import dotenv
import environ
env = environ.Env()
environ.Env.read_env()

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-x51dn5%sqj$rc-#i+-5ivq=#b2u3t7663)0)%xds22fu@c9l$1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG = bool(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = ["*"]
# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "auth_app",
    "plants_app",
    "animals_app",
    "cultures_app",
    "rest_framework",
    "django_filters",
    'drf_spectacular',
    'corsheaders',
    'bootstrap4',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    # add this
    'rest_authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django.contrib.sites',
    #for registration
    #'auth_app.apps.AuthAppConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.google',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #add the middleware for allauth accounts
    'allauth.account.middleware.AccountMiddleware',
    #
]

""" AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

] """

CORS_ALLOWED_ORIGINS = [
    # Add the allowed origins (e.g., frontend URLs)
    'https://fgf-project-frontend.vercel.app', 'http://localhost:5173', 
    'http://localhost:8000',
]

ROOT_URLCONF = "fgf.urls"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "fgf.wsgi.application"

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication', #token generation
        'rest_authtoken.auth.AuthTokenAuthentication',
    )
}

#AUTH_USER_MODEL = 'auth_app.User'

#Domain names to be used
SITE_ID = 1
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'fgf-app-auth' #set name of cookie

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pktpaulie@gmail.com'
EMAIL_USE_SSL = False
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_PASSWORD = 'jjnz bxij sjpw hfzl'

#use email for authentication instead of username
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

#allow the app to verify the user when they open the link received by email
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_GET = True



#registration
REGISTRATION_ENABLED = True


"""
FIREBASE_ACCOUNT_TYPE = os.environ.get('FIREBASE_ACCOUNT_TYPE')
FIREBASE_APIKEY = os.environ.get('FIREBASE_APIKEY')
FIREBASE_AUTH_DOMAIN = os.environ.get('FIREBASE_AUTH_DOMAIN')
FIREBASE_PROJECTID = os.environ.get('FIREBASE_PROJECTID')
FIREBASE_STORAGE_BUCKET = os.environ.get('FIREBASE_STORAGE_BUCKET')
FIREBASE_MESSAGING_SENDERID = os.environ.get('FIREBASE_MESSAGING_SENDERID')
FIREBASE_APPID = os.environ.get('FIREBASE_APPID')
FIREBASE_MEASUREMENTID = os.environ.get('FIREBASE_MEASUREMENTID')
"""


"""config = {
    'apiKey': os.environ.get('FIREBASE_APIKEY'),
    'authDomain': os.environ.get('FIREBASE_AUTH_DOMAIN'),
    'projectId': os.environ.get('FIREBASE_PROJECTID'),
    'storageBucket': os.environ.get('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': os.environ.get('FIREBASE_MESSAGING_SENDERID'),
    'appId': os.environ.get('FIREBASE_APPID'),
    'measurementId': os.environ.get('FIREBASE_MEASUREMENTID')
}"""
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    
"default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db.sqlite3",
    
    # 'ENGINE': 'django.db.backends.postgresql',
    # 'NAME': 'fgf-db',
    # 'USER': 'fgf-app',
    # 'PASSWORD': 'fgf=password',
    # 'HOST': 'localhost',
    # 'PORT': '5432',
    
    }
}

     
 

#DATABASES['default'] = dj_database_url.parse('postgres://fgf_database_user:Hqa4PKjnQGZa33ErpfAYCRpSujZmyp7M@dpg-cka1lbev3ddc739sufb0-a.oregon-postgres.render.com/fgf_database')
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# FOR deployment
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# redirect the user to login-url after verification 
LOGIN_URL = 'http://localhost:8000/login/'
#LOGIN_REDIRECT_URL = 'http://localhost:8000/auth-app/login'
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"