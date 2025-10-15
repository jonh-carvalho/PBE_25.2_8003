"""
Development settings for streaming_platform project.
"""
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Development-specific apps
INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Debug Toolbar
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CORS settings for development
CORS_ALLOW_ALL_ORIGINS = True

# Custom user model
AUTH_USER_MODEL = 'apps.users.User'
