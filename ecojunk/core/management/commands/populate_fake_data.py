from _pytest import junitxml
from django.core.management.base import BaseCommand

from ecojunk.junk.tests.factories import JunkPointRealisticFactory,JunkPointTypeFactory
from ecojunk.junk.constants import TYPES
import random

class Command(BaseCommand):
    help = "Populates database with fake data"

    def handle(self, *args, **options):
        number_of_groups = 100
        types = []
        for tipe in TYPES:
            junktype = JunkPointTypeFactory(name=tipe)
            types.append(junktype)
            junktype.save()
        for l in range(0, number_of_groups):
            batch = []
            for i in range(0, random.randrange(3, 5)):
                extracted = types[random.randrange(0, len(TYPES))]
                while extracted in batch:
                    extracted = types[random.randrange(0, len(TYPES))]
                batch.append(extracted)
            print("junkpoint: " + str(batch))
            junk_point = JunkPointRealisticFactory.build(types=batch)
            junk_point.save()
            print("junkpoint: " + str(junk_point.types))

