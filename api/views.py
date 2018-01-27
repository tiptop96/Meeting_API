from django.shortcuts import render
from api.models import Meeting
from api.serializers import MeetingSerializer
from rest_framework import generics
# Create your views here.
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