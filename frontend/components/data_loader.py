# data_loader.py
import csv

def load_toilet_data():
    toilets = []
    with open('assets/clean_data.csv', mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            toilets.append({
                'name': row['name'],
                'resource_type': row['resource_type'],
                'latitude': float(row['latitude']),
                'longitude': float(row['longitude']),
                'access': row['access'],
                'public_access_hours_open': row['public_access_hours_open'],
                'public_access_hours_close': row['public_access_hours_close'],
                'public_access_days': row['public_access_days'],
                'data_as_of': row['data_as_of'],
                # Add other fields as needed
            })
    return toilets