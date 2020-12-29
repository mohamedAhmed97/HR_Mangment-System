from django.shortcuts import render
from .models import Contract
from .forms import ContractForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def contracts_list(request):
    query_set = Contract.objects.all()
    return render(request, 'contract_list.html', {'contracts': query_set})

def create_contract(request):
    form = ContractForm()
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/employees')
    return render(request, 'create_contract.html', {'form': form})
