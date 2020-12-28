from django.db import models
from employees.models import Employee
# Create your models here.


class LeaveMaster(models.Model):
    leave_name = models.CharField(max_length=55)
    leave_value = models.IntegerField()

    def __str__(self):
        return self.leave_name


class EmployeeLevel(models.Model):
    CONFIRM_CHOICE = (
        ('w', 'waiting'),
        ('a', 'accepted'),
        ('r', 'rejected')
    )
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_id = models.ForeignKey(LeaveMaster, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    confirm=models.CharField(max_length=1, choices=CONFIRM_CHOICE)

    def __str__(self):
        return self.emp_id.full_name
