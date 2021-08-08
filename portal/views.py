from django.shortcuts import render
from  portal.models import Companies
from  portal.models import Testimonials
from  jobs.models import Job_categories
from  jobs.models import Jobs
from  jobs.models import Category
from  portal.models import TopCompanies


def home(request):
    jobs = Job_categories.objects
    jobhome = Jobs.objects
    testi = Testimonials.get_testimonials()
    details = TopCompanies.objects


    data ={}
    data['jobs']= jobs
    data['jobhome'] = jobhome
    data['testi'] = testi
    data['details'] =details
    return render(request,'portal/home.html', data)


def about(request):
    return render(request, 'portal/about.html')

def bjobs(request):
    jobs=None
    items = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        jobs=Jobs.get_all_jobs_by_categoryid(categoryID)
    else:
        jobs = Jobs.get_all_jobs()

    
    data ={}
    data['jobs']= jobs
    data['items'] = items
    return render(request, 'portal/bjobs.html', data)


def companies(request):
    companies = Companies.objects
    return render(request, 'portal/companies.html',{'companies': companies})


def testimonial(request):
    test = Testimonials.objects
    return render(request, 'portal/testimonial.html',{'test':test})

     

   
def terms(request):
     return render(request,'portal/terms.html')  

def faq(request):
     return render(request,'portal/faq.html') 

def companydets(request):
    return render(request,'portal/companydets.html') 
