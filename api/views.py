from django.shortcuts import render
from api.models import Meeting, Region
from api.serializers import MeetingSerializer, RegionSerializer
from rest_framework import generics

class RegionList(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get_queryset(self):
        queryset = Region.objects.all()
        return queryset

#View to handle database queries: path/?<area/region/adress/id>=<searchterm>
class MeetingList(generics.ListAPIView):
    serializer_class = MeetingSerializer

    def get_queryset(self):

        queryset = Meeting.objects.all()
        adress = self.request.query_params.get('adress', None)
        id = self.request.query_params.get('id', None)
        region = self.request.query_params.get('region', None)
        area = self.request.query_params.get('area', None)

        if area is not None:
            queryset = queryset.filter(area__contains=area)
        if region is not None:
            queryset = queryset.filter(region__contains=region)
        if adress is not None:
            queryset = queryset.filter(adress__contains=adress)
        if id is not None:
            queryset = queryset.filter(pk=id)
        return queryset

#Dormant views in case we don't want to use querystrings
class MeetingListById(generics.ListAPIView):
    serializer_class = MeetingSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Meeting.objects.filter(pk=pk)

class MeetingListByArea(generics.ListAPIView):
    serializer_class = MeetingSerializer
    def get_queryset(self):
        pk = self.kwargs['area']
        return Meeting.objects.filter(area__contains=area)