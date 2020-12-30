from django.shortcuts import render
from .models import Contract
from .forms import ContractForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
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
        return HttpResponseRedirect('/contracts')
    return render(request, 'create_contract.html', {'form': form})


def delete_contract(request, con_id):
    contract = Contract.objects.get(id=con_id)
    contract.delete()
    return HttpResponseRedirect('/contracts')


def edit_contract(request, con_id):
    contract = get_object_or_404(Contract, id=con_id)
    if request.method == "POST":
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contracts')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'create_contract.html', {'form': form})
