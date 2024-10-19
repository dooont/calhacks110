# postgreqsl database model for toilets
from app import db

class Toilet(db.Model):
    __tablename__ = 'toilets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    resource_type = db.Column(db.String(50), nullable=False)
    water_fountain = db.Column(db.Boolean)
    bottle_filler = db.Column(db.Boolean)
    jug_filler = db.Column(db.Boolean)
    dog_fountain = db.Column(db.Boolean)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    access = db.Column(db.String(50))
    public_access_hours_open = db.Column(db.Time)
    public_access_hours_close = db.Column(db.Time)
    public_access_days = db.Column(db.String(50))
    data_as_of = db.Column(db.DateTime)
    classification = db.Column(db.String(50))

    # No geography, just latitude and longitude
