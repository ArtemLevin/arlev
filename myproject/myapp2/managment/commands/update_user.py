from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help="Update user name by id"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help='User ID')
        parser.add_argument("name", type=int, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('pk')
        user = User.objects.filter(pk=pk).filter()
        user.name=name
        user.save()
        self.stdout.write(f'{user}')