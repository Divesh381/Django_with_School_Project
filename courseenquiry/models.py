from django.db import models

class courseenquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=50) 
    websiteLink = models.CharField(max_length=70)     
    message = models.TextField()    

    
# Create your models here.
