from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.index, name="principal"),
]
