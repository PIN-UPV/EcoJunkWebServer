from django.core.management.base import BaseCommand
from ecojunk.junk.constants import ACCEPTED
import datetime
from ecojunk.junk.tests.factories import DealFactory


class Command(BaseCommand):
    help = "Creates a deal that has to be automatically republished"

    def handle(self, *args, **options):
       deal = DealFactory(state=ACCEPTED, accepted_date=datetime.datetime.now()-datetime.timedelta(1, 0, 0, 0, 0, 0, 0))
       deal.save()

