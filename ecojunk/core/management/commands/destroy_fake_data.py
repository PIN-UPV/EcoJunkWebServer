from django.core.management.base import BaseCommand
from ecojunk.junk.models import JunkPoint


class Command(BaseCommand):
    help = "Drop database with fake data"

    def handle(self, *args, **options):
        JunkPoint.objects.all().delete()

# sudo docker-compose -f local.yml run django python manage.py populate_fake_data
