from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD

=======
from api.region_area_list import ALL_AREAS, ALL_REGIONS

##Meeting model
>>>>>>> 41d43754735d80ea716a8461f16a525f7fac4445
class Meeting(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, editable=False, on_delete=models.CASCADE)

    name = models.CharField(max_length=96, unique=True, default='')
    description = models.CharField(max_length=196, default='')
    adress = models.CharField(max_length=96, help_text='Street, City, Country (Please activate javascript for autofill)')
<<<<<<< HEAD
=======
    region = models.CharField(max_length=40, choices=ALL_REGIONS, default='N/A') #choices=(('','--------------------'),), default="select"
    area = models.CharField(max_length=40, choices=ALL_AREAS, default='N/A')
>>>>>>> 41d43754735d80ea716a8461f16a525f7fac4445

    def __str__(self):
        return self.name

<<<<<<< HEAD
=======
#When model
>>>>>>> 41d43754735d80ea716a8461f16a525f7fac4445
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