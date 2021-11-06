import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = "Create superuser in command line."

    def add_arguments(self, parser):
        parser.add_argument('--username', '-u', required=True)
        parser.add_argument('--password', '-p', required=True)
        parser.add_argument('--quiet', '-q', action='store_true')

    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(
                username=options['username'],
                password=options['password'],
            )
        except IntegrityError:
            if options['quiet']:
                pass
            else:
                raise
