from django.contrib import admin
from .models import *

# Register your models here.


class NewDevicesAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'device_serial_num', 'device_model', 'origin', 'device_status', 'date_added')

class ReportedDeviceAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'device_serial', 'device_origin', 'device_issue_description', 'date_reported')


admin.site.register(NewDevices, NewDevicesAdmin)
admin.site.register(ReportedDevices, ReportedDeviceAdmin)
admin.site.register(Product)



