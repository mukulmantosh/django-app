from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create Sample User'

    def handle(self, *args, **kwargs):
        if User.objects.filter(username='mukulmantosh').exists() is False:
            User.objects.create_user(username='mukulmantosh', password='admin123',
                                     is_staff=True, is_active=True, is_superuser=True)
