from django.shortcuts import render
from .models import Contract
# Create your views here.


def contracts_list(request):
    query_set = Contract.objects.all()
    return render(request, 'contract_list.html', {'contracts': query_set})
