from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
# class init -> self.date_field.widget.inputtype='data'


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields+(
            "gender","nationality", "address", 
            "first_name","last_name","email",
            "id_type", "id_numbers","hire_date",
            "emp_number","date_of_birth",
            "place_of_birth","social_status",
            "mobile_number","insured","has_medical",
            "role"
        )
        widgets = {
            'date_of_birth': DateInput(),
            'hire_date': DateInput()
        }
