from django.http import HttpResponse
from django.shortcuts import render
from .models import EmployeeLevel

def leaves_list(request):
    query_set = EmployeeLevel.objects.all()
    return render(request, 'employee_level_list.html', {'employees': query_set})
