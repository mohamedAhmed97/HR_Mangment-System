from django.urls import path
from .views import *
urlpatterns = [
    path('leaves/',leaves_list),
    path('leaves/add',create_leaves),
    path('leaves/<con_id>/accept',accept_leave),
    path('leaves/<con_id>/reject',reject_leave),
]