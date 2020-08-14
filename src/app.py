"""
App Start
"""

# Libraries
from flask import Flask

# Configuration
from src.config import config

# Register Protocols
from src.protocols import register_http

# Extension
from src.extensions import register_extensions


def create_app():
    """Create Flask App"""
    app = Flask(__name__)
    app.config.from_object(config)

    register_http(app)
    register_extensions(app)

    return app


def create_worker_app():
    """Minimal App without routes for celery worker."""
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)

    return app
