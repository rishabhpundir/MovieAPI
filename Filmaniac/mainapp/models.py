from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)   

    def __str__(self):
        return self.name + " (" + f"{self.release}" + ")" 


