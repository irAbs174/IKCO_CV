import os


SECRET_KEY = os.environ.get('SECRET_KEY', '<a string of random characters>')

DEBUG = os.environ.get('DEBUG') == "True"

ALLOWED_HOSTS = [os.environ.get('DOMAIN'),]

if DEBUG:
    ALLOWED_HOSTS = ["*",]

SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT') != "False"