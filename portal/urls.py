from django.urls import path, include
from . import views

urlpatterns = [
    
    path('about', views.about , name= 'about'),
    path('bjobs', views.bjobs , name= 'bjobs'),
    path ('companies', views.companies , name= 'companies'),
    path ('testimonial', views.testimonial,name='testimonial'),
    path ('terms', views.terms,name='terms'),
    path ('faq', views.faq,name='faq'),
    path ('companydetails/<int:company_id>', views.companydets,name='companydets'),
  
    path('description/<int:job_id>', views.detail, name='detail'),
    path('catgeory/<int:cat_id>', views.catjobs, name='catjobs'),
    path('search',views.search, name='search'),
    path('search_jobs',views.search_jobs,name='searched'),

  
   

    
    
]