from django.shortcuts import render
from django.http import HttpResponse
from contracts.models import Contract
# Create your views here.

def employees_list(request):
    query_set = Contract.objects.all()
    context = {"employees": query_set}
    return render(request, 'employee_list.html', context)
