from purple.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DATABASES = {
      'default': {
          'ENGINE': 'djongo',
          'NAME': 'purple-meet'
    }
}