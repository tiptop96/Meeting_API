from rest_framework import serializers
from api.models import Meeting, When, Region, Area

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


class AreaSerializer(serializers.ModelSerializer):
    #region = serializers.StringRelatedField(many=True) 
    class Meta:
        model = Area
        fields = ("area_name",)

class RegionSerializer(serializers.ModelSerializer):
    areas = AreaSerializer(many=True)
    class Meta:
        model = Region
        fields = ('region_name', 'areas')