from django.core.management.base import BaseCommand
from ecojunk.junk.models import JunkPoint, JunkPointType


class Command(BaseCommand):
    help = "Drop database with fake data"

    def handle(self, *args, **options):
        JunkPoint.objects.all().delete()
        JunkPointType.objects.all().delete()
