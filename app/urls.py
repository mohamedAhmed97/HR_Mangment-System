from django.urls import path,include
from .views import index
from employees.urls import urlpatterns as employee_urls
from contracts.urls import urlpatterns as contract_urls
urlpatterns=[
    path('home/',index),
    path('',include(employee_urls)),
    path('',include(contract_urls)),
]