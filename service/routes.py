"""
Event Management Service Routes

TODO: Add your REST API routes here
"""

from flask import jsonify
from service.models import db


######################################################################
# GET INDEX
######################################################################
def index():
    """Root URL response"""
    return (
        jsonify(
            name="Event Management REST API Service",
            version="1.0",
            paths="/events",
        ),
        200,
    )
