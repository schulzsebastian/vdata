#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import *
from .. import app


db.init(app.config["DB_NAME"],
        host=app.config["DB_HOST"],
        user=app.config["DB_USER"],
        password=app.config["DB_PASS"],
        port=app.config["DB_PORT"])
if app.config["DB_FLUSH"]:
    try:
        db.drop_table(Features)
    except ProgrammingError:
        pass
db.create_tables([Features], safe=True)
Features.create(geometry="SRID=4326;POINT(1 1)",
                attributes={"key1": "value1", "key2": "value2"})
Features.create(geometry="SRID=4326;POINT(2 2)",
                attributes={"key1": "value1", "key2": "value2"})
