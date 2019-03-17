from django.urls import path
from .views import GetFibo

urlpatterns = [
    path('<int:num>/', GetFibo, name = 'getfibo'),
]
