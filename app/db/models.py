#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import Field, Model, ProgrammingError
from playhouse.postgres_ext import PostgresqlExtDatabase, BinaryJSONField

db = PostgresqlExtDatabase(None, register_hstore=False)


class GeometryField(Field):
    db_field = "geometry"

    def db_value(self, value):
        return str(value)

    def python_value(self, value):
        return str(value)


class Features(Model):
    geometry = GeometryField()
    attributes = BinaryJSONField()

    class Meta:
        database = db
