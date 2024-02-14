from django.db import models
from random import choice


class HeadsAndTailsModel(models.Model):
    SIDE_CONSTANT = "Head", "Tails"

    side = models.CharField(max_length=10, default=choice(SIDE_CONSTANT))
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Результат броска: {self.side}'

    @staticmethod
    def get_info(n):
        info = HeadsAndTailsModel.objects.all()[-n:]
        heads_count = sum(i.side == "Head" for i in info)
        tails_count = n - heads_count
        return {"Head count": heads_count, "Tails count": tails_count}


# Create your models here.


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthdate = models.DateTimeField()
    fullname = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.fullname = f'{self.name} {self.surname}'
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname

class ArticleModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    text = models.TextField()
    publicated = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    publicated_flag =models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    text = models.TextField()
    publicated = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text
