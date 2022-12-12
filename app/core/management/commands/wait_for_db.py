from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as psycopg2operror
import time

class Command(BaseCommand):
    def handle( self, *args , **options):
        self.stdout.write("database not availble")
        dp_up=False

        while dp_up is False:
            try:
                self.check(databases=['default'])
                dp_up=True
            except(psycopg2operror , OperationalError):
                self.stdout.write("database not availble wait for 1 second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("database is available now "))