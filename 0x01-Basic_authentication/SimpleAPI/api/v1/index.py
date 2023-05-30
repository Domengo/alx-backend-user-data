#!/usr/bin/env python3
""" blueprint
    """
from flask import Blueprint, abort

# Create a blueprint for the index module
index = Blueprint('index', __name__)


@index.route('/unauthorized', methods=['GET'])
def unauthorized_route():
    """ Unauthorized endpoint """
    abort(401)


# Add more routes to the blueprint if needed
