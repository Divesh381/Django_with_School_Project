from django.contrib import admin
from serviceDataFilter.models import ServicesDataFilter
class serviceData(admin.ModelAdmin):
    service_data=('servicesDataFilter_icon','servicesDataFilter_title','servicesDataFilter_desc')

admin.site.register(ServicesDataFilter,serviceData)