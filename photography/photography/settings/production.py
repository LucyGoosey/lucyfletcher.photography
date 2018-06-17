from .base import *

DEBUG = False

ALLOWED_HOSTS = ["lucyfletcher.photography","localhost"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
