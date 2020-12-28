from django.urls import path
from .views import Employee_Level_list
urlpatterns = [
    path('ttt',Employee_Level_list)
]