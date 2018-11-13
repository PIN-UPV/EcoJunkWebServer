import random

from django.contrib.gis.geos import Point
from factory.fuzzy import BaseFuzzyAttribute


class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Point(random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0))


class ValenciaPoint(BaseFuzzyAttribute):
    def __init__(self, median, std, **kwargs):
        super(ValenciaPoint, self).__init__(**kwargs)
        self.median = median
        self.std = std

    def fuzz(self):
        return Point(random.gauss(self.median[0], self.std), random.gauss(self.median[1], self.std))
