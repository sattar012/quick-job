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

    



    


    