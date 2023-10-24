"""
Django settings for django_z project.

Generated by 'django-admin startproject' using Django 3.2.22.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d9lw+-p4wiurwx9pe2mfc!%y4mq1xbq_$9mz6%n)k15)pgz_y0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 美化admin界面
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 第三方模块插件
    'import_export',
    'rest_framework',
    'django_q', # 队列任务
    # 安全认证opt
    'django_otp',
    'django_otp.plugins.otp_totp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 用户认证，注意放在用户认证中间件下面
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middleware.IP_delete_can',
]

ROOT_URLCONF = 'django_z.urls'

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

WSGI_APPLICATION = 'django_z.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project_test',
        'USER': 'root',
        'PASSWORD': 'z12138',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

DJANGO_REDIS_CONNECTION_FACTORY = 'django_redis.pool.SentinelConnectionFactory'
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://sentinel-127.0.0.1-6382/5",
        "KEY_PREFIX": '',
        "OPTIONS": {
            "CLIENT_CLASS": 'django_redis.client.SentinelClient',
            "CONNECTION_POOL_KWARGS": {"max_connections": 20},
            "PASSWORD": "umetrip_!1234",
            "SENTINELS": [
                ("127.0.0.1", "6383"),
                ("127.0.0.1", "6383"),
                ("127.0.0.1", "6383"),
            ]
        },
    }
}
CACHE_SECONDS = 60 * 15

Q_CLUSTER = {
    'name': 'DJRedis',
    'workers': 4,
    'timeout': 90,
    'django_redis': 'default'
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
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# simpleui 优化策略
SIMPLEUI_HOME_INFO = False 
SIMPLEUI_ANALYSIS = False 
# opt加密配置，自定义字符配置就行
OTP_TOTP_ISSUER = "otp解码"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 日志格式与日志路径配置
LOG_PATH = os.path.join(BASE_DIR, 'log')

if not os.path.isdir(LOG_PATH):
    os.makedirs(LOG_PATH)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(filename)s %(module)s %(funcName)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'middleware_handler': {
            'level': 'DEBUG',
            'class': 'utils.log_handler.CommonTimedRotatingFileHandler',
            'filename': '%s/middleware.log' % LOG_PATH,
            'formatter': 'simple',
            'backupCount': 3,
            'when': 'midnight',
            'interval': 1
        },
        'middleware_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'middleware_log': {
            'handlers': ['middleware_handler', 'middleware_console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


# REST相关配置
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema' # Api文档配置
}