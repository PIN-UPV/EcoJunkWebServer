from django.core.management.base import BaseCommand
# import random
from ecojunk.junk.tests.factories import JunkPointRealisticFactory


class Command(BaseCommand):
    help = "Populates database with fake data"

    def handle(self, *args, **options):
        # probability_of_multiple_junk_point = 0.3
        # max_neighbour_junk_points = 5
        number_of_groups = 100
        # number_of_junk_points = number_of_groups

        junk_points = []
        for i in range(0, number_of_groups):

            junk_point = JunkPointRealisticFactory()
            junk_points.append(junk_point)
            # if random.random() > (1 - probability_of_multiple_junk_point):
            #     amount = random.randrange(1, max_neighbour_junk_points)
            #     number_of_junk_points += amount
            #     for l in range(0, amount):
            #         JunkPointRealisticFactory(median=junk_point.location, std=0.000004)
