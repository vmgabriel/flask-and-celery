"""
Index Route of Server
"""

# Libraries
from flask import Blueprint, jsonify

# Configure the Route
mod = Blueprint('', __name__)


@mod.route('/')
def base():
    """Route Base"""
    return jsonify({
        'code': 200,
        'message': 'Flask Celery'
    }), 200


@mod.route('/about')
def about():
    """Route for knowledge of creators"""
    return jsonify({
        'code': 200,
        'message': 'About Data - Created By Gabriel Vargas'
    }), 200
