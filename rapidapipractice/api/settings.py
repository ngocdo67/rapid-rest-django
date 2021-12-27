INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes', 
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'api',
  'rest_framework',
]

# Heroku: Update database configuration from $DATABASE_URL. 
import dj_database_url 
import os

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
db_from_env = dj_database_url.config(conn_max_age=500) 
DATABASES['default'].update(db_from_env)