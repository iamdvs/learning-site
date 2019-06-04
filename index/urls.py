from django.urls import path

from .views import *


urlpatterns = [
    path('',index,name="index"),
    path('series/',Seri.as_view(),name="series"),
    path('series/<int:slug>',seriesDetail,name="series_detail"),
]
