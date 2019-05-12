from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
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
            for row in csv_reader:
                try:
                    Position.objects.create(
                        ship=ships[int(row[0])], 
                        date=row[1], 
                        latitude=float(row[2]), 
                        longitude=float(row[3])
                    )
                    imported += 1
                except IntegrityError:
                    pass  

        self.stdout.write(self.style.SUCCESS('Successfully imported "%s" positions.' % imported))
