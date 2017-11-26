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

        if adress is not None:
            queryset = queryset.filter(adress__contains=adress)
        if id is not None:
            queryset = queryset.filter(pk=id)
        return queryset
class MeetingListById(generics.ListAPIView):
    serializer_class = MeetingSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        return Meeting.objects.filter(pk=pk)