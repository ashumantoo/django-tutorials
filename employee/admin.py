from django.contrib import admin

from employee.models import Employee

class AdminEmployee(admin.ModelAdmin):
  list_display = ('first_name','last_name','email','phone_number','designation')
  
# Register your models here.
admin.site.register(Employee, AdminEmployee)
