from django.contrib import admin
from courseenquiry.models import courseenquiry

class courseInfo(admin.ModelAdmin):   
    course_infoDisplay =('name','email','phone','websiteLink','message') 

admin.site.register(courseenquiry,courseInfo);    
# Register your models here.
