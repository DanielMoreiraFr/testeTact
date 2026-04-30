from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import DataModels
from django.core.paginator import Paginator

# Create your views here.

def data_home(request): # mostra tabela com todos os casos
    ordem_dados = DataModels.objects.all().order_by('id') # ordena tudo pelo ID
    paginacao = Paginator(ordem_dados, 50) # cria uma paginaçãp c 50 objetos por pag
    numero_pagina = request.GET.get('page') # pega o número da página atual a partir dos parâmetros da URL
    dados_exibir = paginacao.get_page(numero_pagina) 

    contexto = {
        'dados': dados_exibir 
    }
    return render(request, 'data/home.html', contexto)


def data_remover(request:HttpRequest, id):
    data = get_object_or_404(DataModels, id=id)
    data.delete()
    return redirect('data:home')