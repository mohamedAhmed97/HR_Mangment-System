from django.shortcuts import render
from leaves.models import EmployeeLevel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def index(request):
    query_set = EmployeeLevel.objects.all()
    return render(request,'index.html',{'employees': query_set})
