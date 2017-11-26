from django.conf.urls import url, include
from django.contrib import admin
from api.views import MeetingList
from api.views import MeetingListById
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^meetings/$', MeetingList.as_view()),
    url(r'^meetings/id/(?P<pk>\d+)/$', MeetingListById.as_view()),
]
