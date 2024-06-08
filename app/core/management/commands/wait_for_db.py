"""
Django command to wait for the database to  be available
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Djano command to wait for database"""

    def handle(self, *args, **kwargs):
        """Entrypoint for command."""
        self.stdout.write("Waiting for database...")
        db_up = False

        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database not available, waiting 1 second...")  # noqa
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
