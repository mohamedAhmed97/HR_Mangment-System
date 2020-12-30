from django.http import HttpResponse
from django.shortcuts import render
from .models import EmployeeLevel
from .forms import EmployeeLevelForm
def leaves_list(request):
    query_set = EmployeeLevel.objects.all()
    return render(request, 'employee_level_list.html', {'employees': query_set})

def create_leaves(request):
    form = EmployeeLevelForm()
    if request.method == "POST":
        form = EmployeeLevelForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/home')
    return render(request, 'create_leaves.html', {'form': form})
