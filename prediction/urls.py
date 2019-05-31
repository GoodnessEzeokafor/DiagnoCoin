from django.urls import path, re_path, include
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.prediction, name='prediction'),
    path('form/', views.prediction_view, name='form')
]
