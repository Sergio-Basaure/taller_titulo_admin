from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'usuario',
    'local',
    'productos',
    'servicios',
    'contacto',
    'cliente',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ccs_administrador.urls'

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

WSGI_APPLICATION = 'ccs_administrador.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

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
]

AUTH_USER_MODEL = 'usuario.Usuario' # -> para que utilice el modelo usuario personalizado para la auth

JAZZMIN_SETTINGS = {

    "site_title": "CCS Admin",
    "site_header": "CCS Admin",
    "site_brand": "CCS Admin",
    "welcome_sign": "CCS Admin",
    "copyright": "CCS",
    "site_logo": None,
    "topmenu_links": [
    {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

    
    {"model": "auth.usuario"},

    # App with dropdown menu to all its models pages (Permissions checked against models)
    {"app": "usuario"},
    {"app": "local"},
    {"app": "servicios"},
    {"app": "productos"},
    {"app": "contacto"},
    {"app": "cliente"},

],

    "related_modal_active": True,
    "order_with_respect_to": ["auth", "usuario", "local", "servicio", "producto", "cliente", "contacto"],

    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "carousel",

    "icons": {
        "usuario.usuario": "fas fa-user",
        "local.local": "fas fa-map-marker-alt",
        "contacto.contacto" : "far fa-envelope",
        "productos.categoriaproducto" : "fas fa-certificate",
        "servicios.categoriaservicio" : "fas fa-certificate",
        "local.tiporeclamo" : "fas fa-certificate",
        "cliente.cliente" : "fas fa-user-tie",
        "local.reclamos" : "fas fa-exclamation",
        "productos.producto" : "far fa-dot-circle",
        "servicios.servicio" : "far fa-dot-circle",

    },

}

DATE_INPUT_FORMATS = ['%d-%m-%Y']
TIME_INPUT_FORMATS = ['%H:%M']

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Chile/Continental'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


