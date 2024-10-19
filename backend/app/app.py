# main entry point for running Flask app

# backend/app/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialize extensions without attaching them to the app yet
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import routes or blueprints (import after app is created to avoid circular imports)
    from models import Toilet
    from routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
