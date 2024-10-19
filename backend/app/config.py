# backend/app/config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://toilet:toilet@localhost/toilet_mapper_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add other configurations like S3 credentials, Auth0 credentials, etc.
