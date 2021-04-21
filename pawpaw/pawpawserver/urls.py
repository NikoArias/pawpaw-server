from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pawpawserver import views

urlpatterns = [
    path('', views.papaw_index),
    path('instruments', views.pawpaw_instrument),
    path('time-series-data', views.pawpaw_tsd),
]

urlpatterns = format_suffix_patterns(urlpatterns)
