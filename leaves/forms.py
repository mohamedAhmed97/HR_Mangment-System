from django import forms
from .models import EmployeeLevel
from datetime import date


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeLevelForm(forms.ModelForm):
    class Meta:
        model = EmployeeLevel
        fields = "__all__"
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }

    def check_leave(self, user_id):
        today = date.today()
        last_leave = EmployeeLevel.objects.filter(emp_id=user_id).reverse()
        if len(last_leave) > 0:
            if(today <= last_leave[0].end_date):
                print(last_leave[0].emp_id)
                return False
            else:
                print("true")
                return True
        return True        
