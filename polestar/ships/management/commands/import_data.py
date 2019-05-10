from django.core.management.base import BaseCommand, CommandError
from polestar.ships.models import Position, Ship
from django.db import transaction
from django.conf import settings
import argparse
import sys
import csv
import os


class Command(BaseCommand):
    help = 'Imports ships location data from the assignment.'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=os.path.join(settings.BASE_DIR, '..', 'data', 'positions.csv'))

    def handle(self, *args, **options):
        imported = 0
        ships = {s.imo_number: s for s in Ship.objects.all()}

        self.stdout.write('Importing positions...')
        
        with options.get('file') as f:
            csv_reader = csv.reader(f, delimiter=',')
            with transaction.atomic():
                for row in csv_reader:
                    s = ships[int(row[0])]
                    s.positions.create(date=row[1], latitude=float(row[2]), longitude=float(row[3]))
                    imported += 1

        self.stdout.write(self.style.SUCCESS('Successfully imported "%s" positions.' % imported))
