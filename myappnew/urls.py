from django.contrib import admin
from django.urls import path
from myappnew import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('userlogout/',views.userlogout),
    path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact),
    
]