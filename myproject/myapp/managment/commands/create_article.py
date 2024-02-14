from django.core.management.base import BaseCommand
from myproject.myapp.models import ArticleModel


class Command(BaseCommand):
    help = "Create article."

    def handle(self, *args, **kwargs):
        article = ArticleModel(name='John', email='john@mail.ru', password='secret', age=25)

        article.save()
        self.stdout.write(f'{article}')