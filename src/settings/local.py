from .base import *

import pymysql
pymysql.install_as_MySQLdb()

DEBUG = True

ALLOWED_HOSTS = ["w.ably-test.local"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ably-test",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "ably-test-mysql",
        "PORT": "3306",
        "CONN_MAX_AGE": 60,
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
            "charset": "utf8mb4",
            "use_unicode": True,
        },
    },
}

SESSION_COOKIE_DOMAIN = "ably-test.local"
SESSION_COOKIE_SECURE = False
