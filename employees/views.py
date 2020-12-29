from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def employees_list(request):
    query_set = Employee.objects.all()
    context = {"employees": query_set}
    return render(request, 'employee_list.html', context)

def create_employee(request):
    form=EmployeeForm()
    if request.method=="POST":
        form =EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/employees')
    return render(request,'create_employee.html',{'form':form})