from app import *
from shapely.geometry import shape
import json

with open('static/v.geojson') as f:
    geojson = json.load(open('static/v.geojson'))
data = []
for feature in geojson['features']:
    data.append({
        'geometry': shape(feature['geometry']).wkt,
        'attributes': feature['properties']})
with db.atomic():
    Features.insert_many(data).execute()
