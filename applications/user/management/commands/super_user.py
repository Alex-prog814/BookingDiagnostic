from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Helps create default superuser'

    def handle(self, *args, **options):
        admin = User.objects.create_superuser(email="admin@gmail.com", password="admin")
        print('Created successfully!')
