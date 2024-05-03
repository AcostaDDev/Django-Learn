from django.db import models


class Series(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'
    

class Episode(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    serie = models.ForeignKey(Series, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Episode: {self.number} - {self.name}"

    class Meta:
        verbose_name = 'Episode'
        verbose_name_plural = 'Episodes'
