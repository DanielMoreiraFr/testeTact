from django.shortcuts import render
from data.models import DataModels
from . import utils_dash

def dashboard_home(request):
    contexto = {
        'total_alunos': DataModels.objects.count(),
    }
    
    contexto.update(utils_dash.get_dados_perfil())
    contexto.update(utils_dash.get_dados_tendencias())
    contexto.update(utils_dash.get_dados_idade_pizza())
    contexto.update(utils_dash.get_dados_sono_vs_ansiedade())
    contexto.update(utils_dash.get_dados_trabalho_vs_desempenho())

    return render(request, 'dashboards/home.html', contexto)