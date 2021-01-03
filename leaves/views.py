from django.http import HttpResponse
from django.shortcuts import render
from .models import EmployeeLevel
from .forms import EmployeeLevelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib import messages

def leaves_list(request):
    query_set = EmployeeLevel.objects.all()
    return render(request, 'employee_level_list.html', {'employees': query_set})


""" @receiver(pre_save, sender=EmployeeLevel)
def test_presave(sender, instance, *args, **kwargs):
    instance.emp_id=request.user.id
    print (instance) """


def create_leaves(request):
    form = EmployeeLevelForm()
    if request.method == "POST":
        form = EmployeeLevelForm(request.POST)
        if form.is_valid():
            check_date=form.check_leave(request.user.id)
            if check_date ==True:
                leave=form.save(commit=False)
                leave.emp_id=request.user
                leave.save()
            else:
                messages.error(request, 'You are in aleave!')    

            #print(check_date)
        return HttpResponseRedirect('/leaves')
    return render(request, 'create_leaves.html', {'form': form})
