from django.urls import path
from .views import ListaAlunosAPI, DashboardStatsAPI

app_name = 'api'

urlpatterns = [
    # Endpoint para os dados brutos (paginado)
    path('alunos/', ListaAlunosAPI.as_view(), name='lista-alunos'),
    
    # Endpoint para os chart do dash
    path('dashboard/stats/', DashboardStatsAPI.as_view(), name='stats'),
]