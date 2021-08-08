from django.contrib import admin

# Register your models here.
from .models import Companies
from .models import Testimonials
from .models import TopCompanies



admin.site.register(Companies)

admin.site.register(Testimonials)
admin.site.register(TopCompanies)
