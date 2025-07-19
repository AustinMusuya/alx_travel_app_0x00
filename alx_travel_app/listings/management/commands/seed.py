from django.core.management.base import BaseCommand
from listings.models import Listing
from listings.models import User
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with sample listings using generators"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Seeding listings...'))

        host_users = list(User.objects.filter(is_host=True))
        if not host_users:
            self.stdout.write(self.style.ERROR('No hosts found. Please create host users first.'))
            return

        def generate_listings(n):
            for _ in range(n):
                yield Listing(
                    host=random.choice(host_users),
                    title=fake.sentence(nb_words=5),
                    description=fake.paragraph(nb_sentences=3),
                    location=fake.city(),
                    price_per_night=random.randint(20, 200),
                    max_guests=random.randint(1, 6),
                    available_from=fake.date_this_year(),
                    available_to=fake.date_this_year()
                )

        listings_to_create = list(generate_listings(20))  # or more, depending on your load
        Listing.objects.bulk_create(listings_to_create, batch_size=10)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(listings_to_create)} listings.'))
