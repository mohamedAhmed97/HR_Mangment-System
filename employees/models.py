from django.db import models

# Create your models here.
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
    full_name = models.CharField(max_length=75)
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
    balance=models.IntegerField(
        default=21,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.full_name