from django.http import Http404
from django.shortcuts import render

from employee.models import Employee


# Create your views here.
def employee_details(request,empid):
    try:
        employee = Employee.objects.get(pk=empid)
        context = {
            "employee": employee
        }
        return render(request,'employee_details.html',context)
    except:
        raise Http404