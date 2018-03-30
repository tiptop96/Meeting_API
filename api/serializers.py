from rest_framework import serializers
from api.models import Meeting, When

#Serialize sql data to json

class WhenSerializer(serializers.ModelSerializer):
    class Meta:
        model = When
        fields = ('day', 'time', 'duration')

class MeetingSerializer(serializers.ModelSerializer):
    when = WhenSerializer(many=False)
    class Meta:
        model = Meeting
        fields = ('name', 'description', 'adress', 'when' ,"pk", "region", "area") #'country', 'city',