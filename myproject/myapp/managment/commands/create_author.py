from django.core.management.base import BaseCommand
from myproject.myapp.models import AuthorModel
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = "Create author."

    def handle(self, *args, **kwargs):
        for i in range(5):
            author = AuthorModel(
                name=f'John_{i}',
                surname=f'Snow_{i}',
                email=f'john_{i}@mail.ru',
                bio = lorem_ipsum.words(10),
                password=lorem_ipsum.words(10),
                birthdate = '199{i}-10-10',
                age=25+i
            )
            author.save()
            self.stdout.write(f'{author}')