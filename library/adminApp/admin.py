from django.contrib import admin
from adminApp.models import Admin, SuperAdmin
# Register your models here.

class AdminAdmin(admin.ModelAdmin):
    pass


admin.site.register(Admin, AdminAdmin)
admin.site.register(SuperAdmin, AdminAdmin)