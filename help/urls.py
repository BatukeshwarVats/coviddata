from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.index,name='helphome'),
    path('add/',views.add,name='add'),
    path('add_data/',views.add_data,name='add'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('contactus/',views.contactus,name='contactus')
]