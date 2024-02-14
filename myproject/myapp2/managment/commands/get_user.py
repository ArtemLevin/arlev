from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        # parser.add_arguments('id', type=int, help='User ID')
        parser.add_arguments('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        # id = kwargs['id']
        pk = kwargs['pk']
        # user = User.objects.get(id=id)
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')