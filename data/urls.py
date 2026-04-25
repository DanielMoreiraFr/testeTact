from django.urls import path
from . import views

app_name='data'

urlpatterns = [
    path('', views.data_home, name='home'), # mostra uma tabela com todos os 8000 casos
    path('remover/<int:id>', views.data_remover, name='remover'), # remove um objeto da tabela
]