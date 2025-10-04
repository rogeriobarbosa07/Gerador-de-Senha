from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerador_senha, name='gerador_senha'),
]
