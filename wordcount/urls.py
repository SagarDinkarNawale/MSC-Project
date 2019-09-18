from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home_idintification_Name'),
    path('about/',views.about,name='about_idintification_Name'),#From action name should be count

    path('count/',views.count,name='count_idintification_Name'),#From action name should be count
]

