from django.contrib import admin

from .models import Job_categories
from .models import Jobs
from .models import Category

admin.site.register(Job_categories)
admin.site.register(Jobs)
admin.site.register(Category)