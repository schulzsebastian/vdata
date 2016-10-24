from . import *
from peewee import fn
import unittest


class DbTestCase(unittest.TestCase):
    def test_first_user_value(self):
        value = (Features
                 .select(Features.attributes)
                 .where(Features.id == 1)
                 .dicts())
        self.assertEqual(value[0]["attributes"]["key"], "value")

    def test_first_user_point(self):
        point = (Features
                 .select(fn.ST_AsText(Features.geometry).alias("point"))
                 .where(Features.id == 1)
                 .dicts())
        self.assertEqual(point[0]["point"], "POINT(1 1)")
