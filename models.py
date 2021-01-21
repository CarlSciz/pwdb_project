from django.db import models

# Create your models here.
class Wrestler(models.Model):
    name = models.CharField(max_length=200)
    year_started = models.DateTimeField('year started')
