from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ContractForm(forms.ModelForm):
    class Meta:
        model=Contract
        fields="__all__"
        widgets = {
            'start_date': DateInput(),
        }
        