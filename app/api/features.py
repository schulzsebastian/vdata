#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from peewee import fn
from . import app
from ..db.models import Features
from ..utils.spatial import as_geojson


@app.route("/api/features")
def features():
    features = as_geojson(Features.select(
        fn.ST_AsGeoJson(Features.geometry).alias("geometry"),
        Features.attributes.alias("properties")).dicts())
    return jsonify(features)
