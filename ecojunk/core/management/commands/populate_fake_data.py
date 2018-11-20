from django.core.management.base import BaseCommand

from ecojunk.junk.tests.factories import JunkPointRealisticFactory


class Command(BaseCommand):
    help = "Populates database with fake data"

    def handle(self, *args, **options):
        number_of_groups = 100

        for group in range(number_of_groups):
            JunkPointRealisticFactory()
