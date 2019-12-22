from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.main, name='index'),
    path('registration/', mainapp.registration, name='registration'),

]