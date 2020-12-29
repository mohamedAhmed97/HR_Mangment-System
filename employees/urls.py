from django.urls import path
from .views import *
urlpatterns=[
    path('employees/',employees_list),
    path('employees/add',create_employee),
    path('employees/delete/<emp_id>',delete_employee),
    path('employees/edit/<emp_id>',edit_employee),

]
