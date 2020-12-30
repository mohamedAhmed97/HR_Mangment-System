from django.urls import path
from .views import *
urlpatterns=[
    path('contracts/',contracts_list),
    path('contracts/add',create_contract),
    path('contracts/delete/<con_id>',delete_contract),
    path('contracts/edit/<con_id>',edit_contract)
]
