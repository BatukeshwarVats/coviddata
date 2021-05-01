from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns=[
    path('',views.index,name='helphome'),
    path('add/',views.add,name='add'),
    path('add_data/',views.add_data,name='add'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('contactus/',views.contactus,name='contactus'),
    path('medicines/',views.medicines,name='medicines'),
    path('ambulance/',views.ambulance,name='ambulance'),
    path('consultation/',views.consultation,name='consultation'),
    path('plasma/',views.plasma,name='plasma'),
    path('oxygen/',views.oxygen,name='oxygen'),
    path('tiffin/',views.tiffin,name='tiffin'),
    path('beds/',views.beds,name='beds'),
    path('blood/',views.blood,name='blood'),
    path('others/',views.others,name='others'),
]