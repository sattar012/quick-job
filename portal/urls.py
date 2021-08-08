from django.urls import path, include
from . import views

urlpatterns = [
    
    path('about', views.about , name= 'about'),
    path('bjobs', views.bjobs , name= 'bjobs'),
    path ('companies', views.companies , name= 'companies'),
    path ('testimonial', views.testimonial,name='testimonial'),
    path ('terms', views.terms,name='terms'),
    path ('faq', views.faq,name='faq'),
    path ('companydets', views.companydets,name='companydets'),

    
    
]