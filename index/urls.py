from django.urls import path

from .views import *


urlpatterns = [
    path('',index,name="index"),
    path('series/',Series.as_view(),name="series"),
]
