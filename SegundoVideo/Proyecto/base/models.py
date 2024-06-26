from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    complete = models.BooleanField(default=False, verbose_name='Completo')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        order_with_respect_to = 'user'

