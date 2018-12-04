from _pytest import junitxml
from django.core.management.base import BaseCommand

from ecojunk.junk.tests.factories import JunkPointRealisticFactory, JunkPointTypeFactory
from ecojunk.junk.constants import TYPES
import random


class Command(BaseCommand):
    help = "Populates database with fake data"

    def handle(self, *args, **options):
        number_of_groups = 100
        types = []
        for tipe in TYPES:
            junk_point_type = JunkPointTypeFactory(name=tipe)
            types.append(junk_point_type)
            junk_point_type.save()
        for l in range(0, number_of_groups):
            extracted = []
            for i in range(0, max(0, int(random.gauss(4, 1)))):
                junk_point_type = types[random.randrange(0, len(TYPES))]
                while junk_point_type in extracted:
                    junk_point_type = types[random.randrange(0, len(TYPES))]
                extracted.append(junk_point_type)
            junk_point = JunkPointRealisticFactory.create(types=extracted)  # .build
            junk_point.save()
