from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import DataModels

# Create your views here.

def data_home(request):
    contexto = {
        'dados': DataModels.objects.all()
    }
    return render(request, 'data/home.html', contexto)


def data_remover(request:HttpRequest, id):
    data = get_object_or_404(DataModels, id=id)
    data.delete()
    return redirect('data:home')