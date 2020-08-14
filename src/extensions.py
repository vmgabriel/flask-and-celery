"""
Module of Extension and Data
"""

# Libraries
from celery import Celery

# Const
celery = Celery()


def register_extensions(app):
    """Register and Get Configs"""
    celery.config_from_object(app.config)
