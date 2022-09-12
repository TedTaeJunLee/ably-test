"""
ASGI config for account project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"src.settings.{os.getenv('ENVIRONMENT', default='base')}")

application = get_asgi_application()
