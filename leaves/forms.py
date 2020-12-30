from django import forms
from .models import EmployeeLevel

class DateInput(forms.DateInput):
    input_type = 'date'
class EmployeeLevelForm(forms.ModelForm):
    class Meta:
        model=EmployeeLevel
        fields="__all__"
        widgets = {
            'start_date': DateInput(),
            'end_date':DateInput()
        }
