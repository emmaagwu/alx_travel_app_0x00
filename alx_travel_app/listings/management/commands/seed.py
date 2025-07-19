import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Deleting old listings...'))
        Listing.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Seeding new listings...'))

        for _ in range(20):  # create 20 sample listings
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                price_per_night=random.randint(30, 500),
                location=fake.city(),
                available=random.choice([True, False])
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

        self.stdout.write(self.style.SUCCESS('Seeding complete.'))
