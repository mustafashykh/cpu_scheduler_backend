from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    # url(r'^schedulerHandeler/', views.schedularHandeler),
    url(r'^.*', views.schedularHandeler),
]