from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='my_home'),

     path('about/', views.about, name='about_us'),
    path('contact/', views.contact, name='contact_us'),
    path('services/', views.services, name='services'),
    path ('blog/', views.blog, name='blog'),

]