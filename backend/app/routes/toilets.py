# API endpoints for managing toilets

# backend/app/routes/toilets.py

from flask import Blueprint, request, jsonify
from models.toilet import Toilet
from app import db

# Define the blueprint for API routes
api_blueprint = Blueprint('api', __name__)

# Example route to get all toilets
@api_blueprint.route('/toilets', methods=['GET'])
def get_toilets():
    toilets = Toilet.query.all()
    return jsonify([toilet.to_dict() for toilet in toilets])

# Example route to add a toilet
@api_blueprint.route('/toilets', methods=['POST'])
def add_toilet():
    data = request.json
    toilet = Toilet(
        name=data['name'],
        resource_type=data['resource_type'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        access=data['access'],
        location=f'SRID=4326;POINT({data["longitude"]} {data["latitude"]})'
    )
    db.session.add(toilet)
    db.session.commit()
    return jsonify(toilet.to_dict()), 201
