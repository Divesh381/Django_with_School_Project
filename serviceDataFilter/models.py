from django.db import models
from tinymce.models import HTMLField
class ServicesDataFilter(models.Model):
    servicesDataFilter_icon=models.CharField(max_length=50)
    servicesDataFilter_title=models.CharField(max_length=50)
    servicesDataFilter_desc=HTMLField()

# Create your models here.
