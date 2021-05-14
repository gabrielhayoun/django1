from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=50)
    milliseconds = models.IntegerField(verbose_name='time')
    bytes = models.IntegerField()
    unitPrice = models.FloatField()
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Track'
        ordering = ['name']

    def __str__(self):
        return self.name

class Album(models.Model):
    title= models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Album'
        ordering = ['artist']

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

