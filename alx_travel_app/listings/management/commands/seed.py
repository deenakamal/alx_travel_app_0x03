from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **options):
        sample_listings = [
            {"title": "Beach Resort", "description": "Relax by the sea", "price": 200},
            {"title": "Mountain Cabin", "description": "Escape to the mountains", "price": 150},
            {"title": "City Apartment", "description": "Stay in the city center", "price": 100},
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings!"))
