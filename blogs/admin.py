from django.contrib import admin
from .models import BlogCategory
from .models import CourseType
from .models import Blogs
# Register your models here.

admin.site.register( BlogCategory)

admin.site.register( CourseType)
admin.site.register(Blogs)