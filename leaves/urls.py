from django.urls import path
from .views import leaves_list
urlpatterns = [
    path('leaves/',leaves_list)
]