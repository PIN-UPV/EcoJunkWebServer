from django.core.management.base import BaseCommand
from ecojunk.junk.models import Deal
from ecojunk.junk.constants import ACCEPTED
import datetime


class Command(BaseCommand):
    help = "Menage the deal deadlines"

    def handle(self, *args, **options):
        deals = Deal.objects.filter(
            state=ACCEPTED,
            accepted_date__gt=datetime.datetime.now()
            + datetime.timedelta(1, 0, 0, 0, 0, 0, 0),
        )
        print(str(deals))
