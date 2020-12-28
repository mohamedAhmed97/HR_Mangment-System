from django.http import HttpResponse
from django.shortcuts import render
from .models import EmployeeLevel

def Employee_Level_list(request):
    queryset=EmployeeLevel.objects.all()
    return render(request, 'employee_level_list.html')
