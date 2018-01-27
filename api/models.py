from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, editable=False)

    name = models.CharField(max_length=96, unique=True, default='')
    description = models.CharField(max_length=196, default='')
    adress = models.CharField(max_length=96, help_text='Street, City, Country (Please activate javascript for autofill)')
    region = models.CharField(max_length=40, choices=(('','--------------------'),), default="select")
    area = models.CharField(max_length=40, choices=(('','--------------------'),), default="select")

    def __str__(self):
        return self.name

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