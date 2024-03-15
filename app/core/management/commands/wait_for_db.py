from django.core.management.base import BaseCommand
from django.db import connections
import time
from  django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Wating fir DB connection ...')

        is_db_connected = None
        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Connection Trying ...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('PostgreSQL Connections Success'))