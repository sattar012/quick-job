from django.shortcuts import render, redirect , get_object_or_404
from  .models import Companies
from  .models import Testimonials
from  .models import Job_Category
from  .models import Category
from  .models import Job_details
from  .models import TopCompanies
from  blogs.models import Blogs


def home(request):
    jobs = Job_Category.objects
    allblog =Blogs.objects
    jobhome = Job_details.objects
    testi = Testimonials.get_testimonials()
    details = TopCompanies.objects
    jobcatdetails=None
    catID = request.GET.get('cat_name')
    if catID:
        jobcatdetails = Job_details.get_all_jobs_by_cat_name(catID)
    else:
        jobcatdetails=Job_details.get_all_jobs


    data ={}
    data['jobs']= jobs
    data['jobhome'] = jobhome
    data['testi'] = testi
    data['details'] =details
    data['allblog'] = allblog
    data['jobcatdetails'] =jobcatdetails
    return render(request,'portal/home.html',data ) 


def about(request):
    return render(request, 'portal/about.html')

def bjobs(request):
    jobs=None
    items = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        jobs=Job_details.get_all_jobs_by_categoryid(categoryID)
    else:
        jobs = Job_details.get_all_jobs()
    data ={}
    data['jobs']= jobs
    data['items'] = items
    
    return render(request, 'portal/bjobs.html', data )


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

def companydets(request , company_id):
    company_details = get_object_or_404(TopCompanies, pk=company_id)
    return render (request,'portal/companydets.html', {'company_details': company_details })




def detail(request, job_id): 
    job_detail = get_object_or_404(Job_details,pk=job_id)
    return render(request, 'portal/detail.html',{'job_detail': job_detail})


def catjobs(request,cat_id):
    cat_job_detail = get_object_or_404(Job_Category, pk=cat_id)
    show_jobs = Job_details.objects
    data={}
    data['cat_job_detail'] =cat_job_detail
    data['show_jobs'] =show_jobs

    return render (request, 'portal/catjobs.html',data)


def search(request):
    search = request.GET['search']
    jobs_showjob=Job_details.objects.filter(job_name__icontains=search)
    jobs_showcom= Job_details.objects.filter( company__icontains=search)
    jobs_show = jobs_showjob.union(jobs_showcom)

    params={'jobs_show': jobs_show}
    return render(request,'portal/search.html', params)

def search_jobs(request):
    searched = request.GET['searched']
    name = Job_details.objects.filter(job_name__icontains=searched)
    com= Job_details.objects.filter(company__icontains=searched)
    loc= Job_details.objects.filter(place__icontains=searched)
    search_job= name.union(com,loc)

    detail ={'search_job':search_job}

    return render(request,'portal/searched.html',detail )
        


    
  

   