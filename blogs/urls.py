from django.urls import include, path

from . import views

urlpatterns = [
    
    path('allblogs',views.allblogs , name='allblogs'),
    path('<int:blog_id>', views.blogs, name= 'blogs')
    
    
    
] 