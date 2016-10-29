from app import *
from peewee import fn
from shapely.geometry import shape
import json

def read_geojson(filename):
    with open(filename) as f:
        return json.load(f)


geojson = read_geojson('static/v.geojson')
for feature in geojson['features']:
    Features.create(geometry=shape(feature['geometry']).wkt,
                    attributes=feature['properties'])
