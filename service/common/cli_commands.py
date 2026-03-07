"""
CLI Command Extensions for Flask
"""

from service.models import db


def register(app):
    """Register CLI commands"""

    @app.cli.command("create-db")
    def create_db():
        """Creates the database tables"""
        app.logger.info("Creating database tables...")
        db.create_all()
        app.logger.info("Database tables created.")
