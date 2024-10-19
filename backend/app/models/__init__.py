# backend/app/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .toilet import Toilet  # Import your models here
