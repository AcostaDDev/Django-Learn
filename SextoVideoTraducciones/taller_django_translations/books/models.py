from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, help_text='Título del libro')
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Autor que escribió el libro')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)], help_text='Puntuación general que ha recibido el libro')

    created_at = models.DateTimeField(auto_now_add=True, help_text='Autor que escribió el libro')
    updated_at = models.DateTimeField(auto_now=True, help_text='Autor que escribió el libro')

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'