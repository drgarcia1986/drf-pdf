# encoding: utf-8
from django.conf.urls import patterns, url

from simple.views import SimpleExample
from from_template.views import FromTemplate


urlpatterns = patterns(
    '',
    url(r'^simple/$', SimpleExample.as_view()),
    url(r'^from-template/$', FromTemplate.as_view()),
)
