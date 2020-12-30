from django import forms
from .models import EmployeeLevel

class EmployeeLevelForm(forms.ModelForm):
    class Meta:
        model=EmployeeLevel
        fields="__all__"
