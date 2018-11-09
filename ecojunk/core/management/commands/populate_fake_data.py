from django.core.management.base import BaseCommand
import random
from ecojunk.junk.tests.factories import JunkPointRealisticFactory


class Command(BaseCommand):
    help = "Populates database with fake data"

    def handle(self, *args, **options):
        # jpf = JunkPointRealisticFactory()
        probability_of_multiple_junk_point = 0.3
        max_neighbour_junk_points = 5
        number_of_groups = 100
        number_of_junk_points = number_of_groups
        print_coords = False
        junk_points = []
        for i in range(0, number_of_groups):
            junk_point = JunkPointRealisticFactory()
            junk_points.append(junk_point)
            if not print_coords: print("junk_point: " + str(junk_point))
            if print_coords: print(str(junk_point.location[0]) + "\t" + str(junk_point.location[1]) + "\t" + "circle5")
            if random.random() > (1-probability_of_multiple_junk_point):
                amount = random.randrange(1, max_neighbour_junk_points)
                if not print_coords: print("\t elected for adding " + str(amount) + " junkpoints next to it ")
                number_of_junk_points += amount
                for l in range(0, amount):
                    neighbour = JunkPointRealisticFactory(median=junk_point.location, std=0.000004)
                    if not print_coords: print("\t\t added " + str(neighbour) + " distance: " + str(junk_point.location.distance(neighbour.location)))
                    if print_coords: print(str(neighbour.location[0]) + "\t" + str(neighbour.location[1]) + "\t" + "cross5")
            else:
                if not print_coords: print("\t not elected for adding some junkpoints next to it ")
        if not print_coords:print("Number of total junk points generated: " + str(number_of_junk_points))
        if print_coords: print("You can copy paste the text above to www.copypastemap.com to plot the distribution.")
