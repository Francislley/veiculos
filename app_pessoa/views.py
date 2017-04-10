from multiprocessing import context

from django.shortcuts import render

# Create your views here.
from app_pessoa.models import Tipoveiculo, Marcaveiculo, Veiculo


def index(request):
    lista_de_tipos = Tipoveiculo.objects.all()
    return render(request, 'index.html', context={'lista': lista_de_tipos})

def marca(request):
    mostrarmarca = Marcaveiculo.objects.all()
    return render(request, 'mostrarmarca.html', context={'mostrarmarca': mostrarmarca})

def veiculos(request):
    mostrarveiculo = Veiculo.objects.all()
    return render(request, 'Mostrarveiculo.html', context={'mostrarveiculo': mostrarveiculo})
