from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # Create your models here.

# Create your models here.
User = get_user_model()
# show name of user


def get_user_name(self):
    return self.username


User.add_to_class("__str__", get_user_name)


class Employee(models.Model):
    GENDER_CHOICE = (
        ('F', 'female'),
        ('M', 'male'),
    )
    SOCIAL_CHOICE = (
        ('M', 'married'),
        ('S', 'single')
    )
    ID_CHOICE = (
        ('N', 'national id'),
        ('P', 'passport')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    nationality = models.CharField(max_length=55)
    address = models.CharField(max_length=75)
    id_type = models.CharField(max_length=1, choices=ID_CHOICE)
    id_numbers = models.CharField(max_length=14)
    hire_date = models.DateField('hire_date')
    emp_number = models.CharField(max_length=10)
    date_of_birth = models.DateField('date_of_birth')
    place_of_birth = models.CharField(max_length=75)
    social_status = models.CharField(max_length=1, choices=SOCIAL_CHOICE)
    mobile_number = models.CharField(max_length=11)
    insured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    has_medical = models.BooleanField(default=False)
    balance = models.IntegerField(
        default=21,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.username
