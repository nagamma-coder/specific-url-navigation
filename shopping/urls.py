from django.urls import path
from shopping.views import *
app_name='shopping'
urlpatterns=[
    path('texttiles/',texttiles,name='texttiles'),
]