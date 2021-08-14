from django.contrib import admin

# Register your models here.
from .models import Companies
from .models import Testimonials
from .models import TopCompanies
from .models import Job_Category
from .models import Category
from .models import Job_details


admin.site.register(Companies)

admin.site.register(Testimonials)
admin.site.register(TopCompanies)
admin.site.register(Job_Category)
admin.site.register(Category)
admin.site.register(Job_details)
