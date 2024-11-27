from django.core.management.utils import get_random_secret_key
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Generate your secret key'

    def handle(self, *args, **options):
        self.stdout.write('Tu SECRET_KEY es:')
        self.stdout.write(get_random_secret_key())