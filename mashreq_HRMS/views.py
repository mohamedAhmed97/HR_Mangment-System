from django.shortcuts import render
from leaves.models import EmployeeLevel

def index(request):
    query_set = EmployeeLevel.objects.all()
    return render(request,'index.html',{'employees': query_set})
