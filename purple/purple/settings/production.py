from purple.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]