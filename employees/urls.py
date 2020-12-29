from django.urls import path
from .views import *
urlpatterns=[
    path('employees/',employees_list),
    path('employees/add',create_employee)
]
