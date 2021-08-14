from django.db import models

# Create your models here.
class Companies(models.Model):
    image = models.ImageField(upload_to = 'images/')
    Companies=models.CharField(max_length=200)
    url = models.TextField()

    def __str__(self):
          return "Company Name : "+ self.Companies


class Testimonials(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    job= models.CharField(max_length=255)

    def __str__(self):
          return "Testimonial from : "+ self.title


    @staticmethod
    def get_testimonials():
        return Testimonials.objects.all()[:3]
    


class TopCompanies(models.Model):
    icon = models.ImageField(upload_to = 'images/')
    companyName = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)
    description = models.TextField()
    founddate = models.CharField(max_length=100)
    founder = models.CharField(max_length=100)
    revenue = models.CharField(max_length=50)
    employees =models.CharField(max_length=50)
    url = models.TextField()

    def __str__(self):
        return "company name : "+self.companyName

    
class Job_Category(models.Model):
    cat_image = models.ImageField(upload_to = 'images/')
    cat_name =  models.CharField(max_length=100)
    cat_url = models.TextField(blank=True)

    def __str__(self):
        return self.cat_name


class Category(models.Model):
    name = models.CharField(max_length=200)
    category_url = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

class Job_details(models.Model):
    job_name = models.CharField(max_length=200)
    jobtype =  models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,default = 1)
    cat_name = models.ForeignKey(Job_Category, on_delete=models.CASCADE,default=1)
    company = models.CharField(max_length=200)
    skills  = models.CharField(max_length=200)
    experience = models.CharField(max_length=100 , default=" ")
    salary = models.CharField(max_length=200)
    place  = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    phonenumber = models.CharField(max_length=20,)
    jobdescription= models.TextField()
    jobid = models.IntegerField()
    jobview =models.IntegerField(blank=True)
    placeurl= models.TextField(blank=True)

    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %Y ')

    def __str__(self):
        return "Job name : "+self.job_name

    @staticmethod
    def get_all_jobs():
        return Job_details.objects

    @staticmethod
    def get_all_jobs_by_categoryid(category_id):
        if category_id:
            return Job_details.objects.filter(category=category_id)
        else:
            return Job_details.get_all_jobs()


    # @staticmethod
    # def get_all_jobs_by_categorytypeid(categorytype_id):
    #     if categorytype_id:
    #         return Job_details.objects.filter(cat_name=categorytype_id)
    #     else:
    #         return Job_details.get_all_jobs()


    


    