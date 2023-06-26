from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('choose', views.choose, name='choose'),
    path('classes', views.classes, name='classes'),
    path('contact', views.contact, name='contact'),
    path('contactuser', views.contactuser, name='contactuser'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
    path('register', views.register, name='register'),
    path('reg',views.reg,name='reg'),
    path('login', views.login, name='login'),
    path('log', views.log, name='log'),
    path('career', views.career, name='career'),
    path('apply', views.apply, name='apply'),
    path('aply', views.aply, name='aply'),

]