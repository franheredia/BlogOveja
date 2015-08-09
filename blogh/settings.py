import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '5w2+695+h#bkl!&kd8qjrezpyz&#*__lj!m7$b_f2xy%wxg5nh'

DEBUG = True

TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pagina',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'blogh.urls'
WSGI_APPLICATION = 'blogh.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#Rutas
STATIC_URL = '/static/'
MEDIA_URL = '/imagenes/'
STATIC_ROOT = BASE_DIR + '/static/'
MEDIA_ROOT = BASE_DIR + '/imagenes/'

#Configuracion para los emails
EMAIL_HOST="smtp.live.com"
EMAIL_PORT=587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''