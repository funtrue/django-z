from django.contrib import admin
from demo_test.models import Demo_Model
from import_export.admin import ImportExportModelAdmin

class Demo_Model_machineAdmin(ImportExportModelAdmin):
    list_display = ('demo_ip', 'demo_app_name', 
                    'demo_status', 'demo_Duration', 'demo_allocation_time')
    search_fields = ('demo_ip', )
    list_filter = ("demo_Duration","demo_status",)

admin.site.register(Demo_Model,Demo_Model_machineAdmin)
