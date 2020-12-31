from django.urls import path, include
from .views import index
from employees.urls import urlpatterns as employee_urls
from contracts.urls import urlpatterns as contract_urls
from leaves.urls import urlpatterns as leaves_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('home/', index),
    path('', include(employee_urls)),
    path('', include(contract_urls)),
    path('', include(leaves_urls))
]
