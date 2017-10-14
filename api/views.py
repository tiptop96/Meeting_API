from django.shortcuts import render
from api.models import Meeting
from api.serializers import MeetingSerializer
from rest_framework import generics
# Create your views here.
class MeetingList(generics.ListAPIView):
    serializer_class = MeetingSerializer

    def get_queryset(self):

        queryset = Meeting.objects.all()
        country = self.request.query_params.get('country', None)
        city = self.request.query_params.get('city', None)
        if country is not None:
            queryset = queryset.filter(country=country)
        if city is not None:
            queryset = queryset.filter(city=city)
        return queryset
