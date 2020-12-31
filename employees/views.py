from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.


def employees_list(request):
    query_set = User.objects.all().filter(is_superuser=False)
    context = {"employees": query_set}
    return render(request, 'employee_list.html', context)


def create_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/employees')
    return render(request, 'create_employee.html', {'form': form})


def delete_employee(request, emp_id):
    employee = User.objects.get(id=emp_id)
    employee.delete()
    return HttpResponseRedirect('/employees')


def edit_employee(request, emp_id):
    employee = get_object_or_404(Employee, user_id=emp_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'create_employee.html', {'form': form})
