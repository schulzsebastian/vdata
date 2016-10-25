#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import app, jsonify
from .. import Features
from peewee import fn
import json

def as_geojson(features):
    data = {
        'type': 'FeatureCollection',
        'features': []
    }
    for feature in features:
        feature['geometry'] = json.loads(feature['geometry'])
        feature['type'] = 'Feature'
        data['features'].append(feature)
    return data

@app.route('/api/features')
def features():
    features = as_geojson(Features.select(
        fn.ST_AsGeoJson(Features.geometry).alias('geometry'),
        Features.attributes.alias('properties')).dicts())
    return jsonify(features)
