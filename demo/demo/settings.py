"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UUIDUSER_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'uuiduser'))
if UUIDUSER_DIR not in sys.path:
  sys.path.insert(0, UUIDUSER_DIR)


# UUIDUser Settings
# =================

INSTALLED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  # Must come before django.contrib.auth if you want to override the
  # createsuperuser command.
  'uuiduser',

  # This is a custom app we made to hold the subclassed UUIDUser.
  # You can name it anything you want, or put your user model somewhere else.
  'users',
)

# To swap the User model you must declare it here.  It's easiest to do this at
# the beginning of a project.  For more information, see Django's docs on
# swapping the User model:
#
# https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#specifying-a-custom-user-model

AUTH_USER_MODEL = 'users.User'


AUTHENTICATION_BACKENDS = (
  'uuiduser.backends.UUIDUserBackend',

  # Login by username in Django admin
  # 'django.contrib.auth.backends.ModelBackend',
)

# Regular Django Settings
# =======================

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&5(zagh-89va=(9a*fc9t66hev%w%e7k@&a=c9g6ey=+mp&oqk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'demo.urls'

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

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
