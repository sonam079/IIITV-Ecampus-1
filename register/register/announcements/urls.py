from django.conf.urls import url, include
from .views import announcement_upload, AnnouncementView

urlpatterns = [
    url(r'^$', announcement_upload, name='announcement_upload'),
    url(r'^view/$', AnnouncementView.as_view(), name='announcement_view'),
]