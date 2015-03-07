from django.conf.urls import patterns, url
from simple.views import SimpleExample


urlpatterns = patterns(
    '',
    url(r'^simple/$', SimpleExample.as_view()),
)
