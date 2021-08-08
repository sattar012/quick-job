from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone= models.CharField(max_length=13)
    email= models.CharField(max_length=100)
    subject= models.CharField(max_length=200)
    message= models.TextField()

    def __str__(self):
          return "Message from " + self.name + ' - ' + self.email 


     
     

