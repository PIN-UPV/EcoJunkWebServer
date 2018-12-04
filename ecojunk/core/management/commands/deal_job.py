from django.core.management.base import BaseCommand
from ecojunk.junk.models import Deal
from ecojunk.junk.constants import ACCEPTED, PUBLISHED
import datetime


class Command(BaseCommand):
    help = "Menage the deal deadlines"

    def handle(self, *args, **options):
        print("########################################")
        print("############### DEAL JOB ###############")
        print("########################################")

        deals = Deal.objects.filter(state=ACCEPTED, accepted_date__lt=datetime.datetime.now()-datetime.timedelta(1, 0, 0, 0, 0, 0, 0))
        for deal in deals:
            deal.state = PUBLISHED
            deal.accepted_date = None
            deal.save()


