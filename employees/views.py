from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def employees_list(request):
    query_set = User.objects.all().filter(is_superuser=False)
    context = {"employees": query_set}
    return render(request, 'employee_list.html', context)


@login_required
def create_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
    return render(request, 'create_employee.html', {'form': form})


@login_required
def delete_employee(request, emp_id):
    employee = User.objects.get(id=emp_id)
    employee.delete()
    return HttpResponseRedirect('/employees')


@login_required
def edit_employee(request, emp_id):
    employee = get_object_or_404(User, user_id=emp_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'create_employee.html', {'form': form})
