"""
Log Handlers

Provides logging setup for the application
"""

import logging


def init_logging(app, gunicorn_logger="gunicorn.error"):
    """Set up logging for production"""
    app.logger.handlers = logging.getLogger(gunicorn_logger).handlers
    app.logger.setLevel(logging.INFO)
    app.logger.propagate = False
    app.logger.info("Logging handler established")
