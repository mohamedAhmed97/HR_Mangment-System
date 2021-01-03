from django.db import models
from employees.models import User

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=55)
    department_desc = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.department_name


class Position(models.Model):
    position_name = models.CharField(max_length=55)

    def __str__(self):
        return self.position_name


class Contract(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    dep_id = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    pos_id = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    start_date = models.DateField()
    end_date = models.DateField(
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user_id.first_name

    def get_end_date_value(self):
        if self.end_date is None:
            return "Still Working"
        return self.end_date
