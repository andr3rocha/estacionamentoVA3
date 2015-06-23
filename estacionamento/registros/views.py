#coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from .models import cliente,carro,vaga,alugarvaga
from .forms import formCarro, formVaga, formCliente, formReserva



def index(request):
	context = {'texto': 'Projeto Django Estacionamento'}
	
	return render(request, 'index.html', context)
 


def viewCadastroCliente(request, id=None): 
    if id == None:
        obj = None
    else:
        obj = get_object_or_404(cliente,pk=id)

    if request.method == 'POST':
        form = formCliente(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            q = cliente.objects.all()
            context ={
            'listacliente': q,
                        }
            return render(request, 'clientecadastrados.html', context) 
    else:
        form = formCliente(instance=obj)

    return render(request, "cadastroCliente.html", {'form': form})


def viewCadastroCarro(request,id=None):

    if id == None:
        obj = None
    else:
        obj =get_object_or_404(carro,pk=id)

    if request.method == 'POST':
        form = formCarro(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            q = carro.objects.all()
            context ={
            'listacarro': q,
            }
            return render(request, 'carroscadastrados.html', context)
    else:
        form = formCarro(instance=obj)

    return render(request, "cadastroCarro.html", {'form': form})



def viewCriarVaga(request,id=None):

    if id==None:
        obj=None
    else:
        obj = get_object_or_404(vaga,pk=id)

    if request.method == 'POST':
        form = formVaga(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            q = vaga.objects.all()
            context = {
            'listavaga': q,
            }
            return render(request, 'vagascadastradas.html', context) 
    else:
        form = formVaga(instance=obj)

    return render(request, "criarVaga.html", {'form': form})



def viewCriarReserva(request,id=None):
    if id==None:
        obj=None
    else:
        obj = get_object_or_404(alugarvaga,pk=id)

    if request.method == 'POST':
        form = formReserva(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            q = alugarvaga.objects.filter(temposaida=None)
            context = {
            'listareserva' : q,
            }

            return render(request, "vagasalugadas.html", context)
    else:
       form = formReserva(instance=obj)

    return render(request, 'Reserva.html', {'form': form})


##############################################################################

def inserirReserva(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        w = cliente.objects.filter(Nome__contains=query)
        if w:
            q = alugarvaga.objects.filter(temposaida=None,cliente=w)
    else:
        q = alugarvaga.objects.filter(temposaida=None)

    context = {
    'listareserva' : q,
    }

    return render (request, "vagasalugadas.html",context)

def inserirClientesCadastrados(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        q = cliente.objects.filter(Nome__contains=query)
    else:
        q = cliente.objects.all()
     
    context = {
    'listacliente': q,
    }

    return render (request,"clientecadastrados.html",context)

def inserirVagasCadastradas(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        q = vaga.objects.filter(NomeVaga__contains=query)
    else:
        q = vaga.objects.all()
    context = {
    'listavaga': q,
    }

    return render (request,"vagascadastradas.html",context)

def inserirCarrosCadastrados(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        q = carro.objects.filter(Marca__contains=query)
    else:
        q = carro.objects.all()
    context = {
    'listacarro': q,
    }
    return render (request,"carroscadastrados.html",context) 

