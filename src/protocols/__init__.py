"""
Package of Protocols
"""

# Modules
from flask import Flask
from src.protocols.http import http_v0_index


def register_http(app: Flask) -> None:
    """Register All Http"""
    app.register_blueprint(http_v0_index, url_prefix='/api')
