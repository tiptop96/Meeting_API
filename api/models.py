from django.db import models

class Meeting(models.Model):
    name = models.CharField(max_length=96, unique=True, blank=True)
    
    country = models.CharField(max_length=96)
    city = models.CharField(max_length=96)
    street = models.CharField(max_length=96)

    start_time = models.TimeField(max_length=96, blank=True)
    end_time = models.TimeField(max_length=96, blank=True)

    #DAYS
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Create your models here.
