from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Serie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Episode(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    serie = models.ForeignKey(Serie, on_delete=CASCADE)

    def __str__(self):
        return f'{self.name} - {self.number}'


class Score(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=CASCADE)
    serie = models.ForeignKey(Serie, on_delete=CASCADE)
    episode = models.ForeignKey(Episode, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return f"User -> {self.user} ,Score -> {self.score}"
