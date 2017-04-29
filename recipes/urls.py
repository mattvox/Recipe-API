from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.recipes),  # ^ -> start of something; $ -> end
    url(r'^(?P<recipe_id>[0-9]+)/$', views.detail),
]
