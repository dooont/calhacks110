import csv
from app import create_app, db
from models.toilet import Toilet
from datetime import datetime

def import_data(csv_file):
    app = create_app()  # Create the Flask app instance
    with app.app_context():  # Use the application context to access the database
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                toilet = Toilet(
                    name=row['name'],
                    resource_type=row['resource_type'],
                    water_fountain=bool(int(row['water_fountain'])),
                    bottle_filler=bool(int(row['bottle_filler'])),
                    jug_filler=bool(int(row['jug_filler'])),
                    dog_fountain=bool(int(row['dog_fountain'])),
                    latitude=float(row['latitude']),
                    longitude=float(row['longitude']),
                    access=row['access'],
                    public_access_hours_open=datetime.strptime(row['public_access_hours_open'], '%H:%M:%S').time() if row['public_access_hours_open'] else None,
                    public_access_hours_close=datetime.strptime(row['public_access_hours_close'], '%H:%M:%S').time() if row['public_access_hours_close'] else None,
                    public_access_days=row['public_access_days'],
                    data_as_of=datetime.strptime(row['data_as_of'], '%Y/%m/%d %I:%M:%S %p') if row['data_as_of'] else None,
                    location=f'SRID=4326;POINT({row["longitude"]} {row["latitude"]})'
                )
                db.session.add(toilet)
        db.session.commit()

if __name__ == '__main__':
    import_data('data/clean_data.csv')

