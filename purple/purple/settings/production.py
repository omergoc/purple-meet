from purple.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]


STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
      'default': {
          'ENGINE': 'djongo',
          'NAME': 'purple-meet',
           'CLIENT': {
                'host': '192.168.212.170',
                'port': 27017,
        }
    }
}