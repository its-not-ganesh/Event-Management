"""
Module: error_handlers
"""

from flask import jsonify
from service.models import DataValidationError


def init_error_handlers(app):
    """Initialize error handlers for the Flask app"""

    @app.errorhandler(DataValidationError)
    def request_validation_error(error):
        """Handles Value Errors from bad data"""
        return jsonify(status=400, error="Bad Request", message=str(error)), 400

    @app.errorhandler(404)
    def not_found(error):
        """Handles resources not found"""
        return (
            jsonify(status=404, error="Not Found", message=str(error)),
            404,
        )

    @app.errorhandler(405)
    def method_not_allowed(error):
        """Handles method not allowed"""
        return (
            jsonify(status=405, error="Method Not Allowed", message=str(error)),
            405,
        )

    @app.errorhandler(415)
    def mediatype_not_supported(error):
        """Handles unsupported media requests"""
        return (
            jsonify(
                status=415,
                error="Unsupported media type",
                message=str(error),
            ),
            415,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        """Handles unexpected server errors"""
        return (
            jsonify(
                status=500,
                error="Internal Server Error",
                message=str(error),
            ),
            500,
        )
