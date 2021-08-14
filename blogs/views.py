from django.shortcuts import render, redirect , get_object_or_404
from .models import BlogCategory
from .models import CourseType
from .models import Blogs


# Create your views here.

def allblogs(request):
    category= BlogCategory.objects
    allpost =Blogs.objects

    data={}
    data['category'] = category
    data['allpost'] = allpost

    return render(request,'blogs/allblogs.html',data)


def  blogs(request, blog_id):
    blog_details = get_object_or_404( Blogs, pk=blog_id)

    return render(request, 'blogs/blogs.html',{ 'blog_details': blog_details})

