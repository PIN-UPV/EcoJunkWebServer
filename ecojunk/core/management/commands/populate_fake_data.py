from django.core.management.base import BaseCommand
import random

from ecojunk.junk.tests.factories import JunkPointRealisticFactory
from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = "Populates database with fake data"

    def handle(self, *args, **options):
        # jpf = JunkPointRealisticFactory()
        probability_of_multiple_junk_point = 0.3
        max_neighbour_junk_points = 5
        number_of_groups = 70
        number_of_junk_points = number_of_groups
        junk_points = []
        for i in range(0, number_of_groups):
            junk_point = JunkPointRealisticFactory()
            junk_points.append(junk_point)
            print("junk_point: " + str(junk_point))
            if random.random() > (1-probability_of_multiple_junk_point):
                amount = random.randrange(1, max_neighbour_junk_points)
                print("\t elected for adding " + str(amount) + " junkpoints next to it ")
                number_of_junk_points += amount
                for l in range(0, amount):
                    neighbour = JunkPointRealisticFactory(median=junk_point.location, std=0.00001)
                    print("\t\t added " + str(neighbour) + " distance: " + str(junk_point.location.distance(neighbour.location)))
            else:
                print("\t not elected for adding some junkpoints next to it ")
        print("Number of total junk points generated: " + str(number_of_junk_points))
# sudo docker-compose -f local.yml run django python manage.py populate_fake_data
