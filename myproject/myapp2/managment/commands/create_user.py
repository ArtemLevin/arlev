from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "create user."

    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@mail.ru', password='secret', age=25)

        user.save()
        self.stdout.write(f'{user}')