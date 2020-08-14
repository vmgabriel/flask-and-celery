
"""
Package of Configuration
"""
# Libraries
import os

# Modules
from src.config.flask import configuration as flask_config
from src.config.celery import configuration as celery_config


BASEDIR = os.path.abspath(os.path.dirname(__name__))
print(BASEDIR)


class Config(object):
    """Configuration Service"""
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(16).hex())

    CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE", "America/Bogota")
    BROKER_URL = os.getenv("BROKER_URL", "redis://localhost:6379/0")
    CELERY_SEND_SENT_EVENT = True


class DevelopmentConfig(Config):
    """Development Configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production Config"""


# return active config
available_configs = dict(
    development=DevelopmentConfig,
    production=ProductionConfig
)
selected_config = os.getenv(
    "FLASK_ENV",
    "production"
)
config = available_configs.get(
    selected_config,
    "production"
)
