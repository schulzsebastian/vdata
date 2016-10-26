#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def as_geojson(features):
    data = {
        "type": "FeatureCollection",
        "features": []
    }
    for feature in features:
        feature["geometry"] = json.loads(feature["geometry"])
        feature["type"] = "Feature"
        data["features"].append(feature)
    return data
