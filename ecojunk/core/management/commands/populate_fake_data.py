from django.core.management.base import BaseCommand

from ecojunk.junk.tests.factories import JunkPointFactory


class Command(BaseCommand):
    help = "Populates database with fake data"

    def handle(self, *args, **options):
        JunkPointFactory.create_batch(size=10)
