from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
my_SECRET_KEY = 'django-insecure-@)@vzsn(vs(cwzps=ov%9#6vv)a(0z63vk)l@nr)o^uev^=05h'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

my_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mysql',
#         'USER' : 'root',
#         'PASSWORD' : '12341234',
#         'HOST' : '127.0.0.1',
#         'PORT' : '3305'
#     }
}

