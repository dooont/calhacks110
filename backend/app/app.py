# main entry point for running Flask app

# backend/app/app.py

from flask import Flask
from config import Config
from models import db
from routes import api_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    CORS(app)  # Enable Cross-Origin Resource Sharing for API endpoints

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
