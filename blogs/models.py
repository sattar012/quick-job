from django.db import models
from django.contrib.auth.models import User



class BlogCategory(models.Model):
    BlogRelated = models.CharField(max_length=200)
    
    
    
    def __str__(self):
        return self.BlogRelated

class CourseType(models.Model):
    coursetype =models.CharField(max_length=200)

    def __str__(self):
        return self.coursetype


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    program = models.ForeignKey(CourseType, on_delete=models.CASCADE,default=1)
    Relate= models.ForeignKey(BlogCategory, on_delete=models.CASCADE,default=1)
    publis_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    simage = models.ImageField(upload_to='images/')
    sbody =  models.TextField()
    url= models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE ,default=1)

    def __str__(self):
        return self.title

    def pub_date(self):
        return self.publis_date.strftime(' %b %e %Y ')

    def smallbody(self):
        return self.sbody[:100]

