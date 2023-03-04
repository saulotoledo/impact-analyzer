from django.core.management.base import BaseCommand
from tags.seeders import seed_tags_table

class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **options):
        seed_tags_table()
        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
