#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from .. import app


@app.route("/api/status")
def status():
    return jsonify({"status": "ok"})
