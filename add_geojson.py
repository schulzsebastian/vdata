from app import *
from shapely.geometry import shape
import json

with open('static/v.geojson') as f:
    geojson = json.load(f)

with db.atomic():
    for feature in geojson['features']:
        Features.create(geometry=shape(feature['geometry']).wkt,
                        attributes=feature['properties'])
