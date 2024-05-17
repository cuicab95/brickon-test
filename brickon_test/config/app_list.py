DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MY_APPS = [
    'brickon_test.apps.security',
]
EXTERNAL_APPS = [
    'rest_framework',
    'drf_yasg',
]
INSTALLED_APPS = DJANGO_APPS + MY_APPS + EXTERNAL_APPS