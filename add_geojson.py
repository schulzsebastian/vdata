from app import *
import json

def read_geojson(filename):
    with open(filename) as f:
        return json.load(f)


geojson = read_geojson('static/v.geojson')
i = 0
for feature in geojson['features']:
    i += 1
print i
