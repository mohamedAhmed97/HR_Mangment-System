from django import forms
from .models import Employee

#class init -> self.date_field.widget.inputtype='data'

class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'date_of_birth': DateInput(),
            'hire_date':DateInput()
        }
