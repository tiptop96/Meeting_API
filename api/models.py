from django.db import models
from django.contrib.auth.models import User
from api.region_area_list import ALL_AREAS, ALL_REGIONS

class Region(models.Model): 
    region_name = models.CharField(max_length=90)

    def __str__(self):
        return self.region_name
    
class Area(models.Model):
    area_name = models.CharField(max_length=120)
    region = models.ForeignKey(Region, related_name='areas', on_delete=models.CASCADE, null=True)

class Meeting(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE)

    name = models.CharField(max_length=96, unique=True, default='')
    description = models.CharField(max_length=196, default='')
    country = models.CharField(max_length=96, null=False)
    city = models.CharField(max_length=96, null=False)
    street = models.CharField(max_length=96, null=False)
    longlat = models.CharField(max_length=96, null=False)
    formatted_address = models.CharField(max_length=196, null=False)
    #adress = models.CharField(max_length=96, help_text='Street, City, Country (Please activate javascript for autofill)')
    region = models.CharField(max_length=40, choices=ALL_REGIONS, default='N/A')
    area = models.CharField(max_length=40, choices=ALL_AREAS, default='N/A')

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(Meeting, self).__init__(*args, **kwargs)
        self._meta.get_field('region')._choices = Region.objects.values_list()
        self._meta.get_field('area')._choices = Area.objects.values_list()

#When model
class When(models.Model):
    DAYS = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thusday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    )
    day = models.CharField(max_length=10, choices=DAYS, default='Monday')
    time = models.TimeField(default='19:00:00')
    duration = models.CharField(help_text='In minutes', max_length=3, default=60)
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, null=True)

    #class Meta:
     #   unique_together = ('meeting')

