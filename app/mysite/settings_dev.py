"""
settings for development environment
"""

# pylint: disable=wildcard-import,unused-wildcard-import
import os
from .settings import *  # noqa: F403

SECRET_KEY = 'a50c5005ce62971bcddb7457d7a27b7957024aead3dbe001d67eed170c6fc2e8'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}
