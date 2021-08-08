from django.db import models


# Create your models here.

class Job_categories(models.Model):
    image = models.ImageField(upload_to = 'images/')
    type = models.CharField(max_length=200)

    def __str__(self):
          return "Category  :" + self.type


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    

   
class Jobs(models.Model):
    title = models.CharField(max_length=200)
    jobtype =  models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,default = 1)
    company = models.CharField(max_length=200)
    skills  = models.CharField(max_length=200)
    experience = models.IntegerField(default= 0)
    salary = models.CharField(max_length=200)
    place  = models.CharField(max_length=200)

    @staticmethod
    def get_all_jobs():
        return Jobs.objects.all

    @staticmethod
    def get_all_jobs_by_categoryid(category_id):
        if category_id:
            return Jobs.objects.filter(category=category_id)
        else:
            return Jobs.get_all_jobs()



        

    

    
    



   



   

    





