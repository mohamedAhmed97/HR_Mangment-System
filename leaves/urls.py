from django.urls import path
from .views import *
urlpatterns = [
    path('leaves/',leaves_list),
    path('leaves/add',create_leaves)
]