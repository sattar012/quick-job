from django.shortcuts import render
from portal.models import Testimonials


# Create your views here.
def dashboard(request):
    test = Testimonials.objects

    data={}
    data['test'] = test
    return render (request,'pluto/dashboard.html',data)