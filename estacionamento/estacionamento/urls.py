#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns = [  
    # Examples:
    #url(r'^$', 'estacionamento.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$','registros.views.index',name='home'),

    url(r'^home/estacionamento/carro/$','registros.views.viewCadastroCarro',name='carro'),
    url(r'^home/estacionamento/carro/editarcarros/(?P<id>[0-9]+)/$','registros.views.viewCadastroCarro',name='editarcarros'),
    url(r'^home/estacionamento/listarcarros/$','registros.views.inserirCarrosCadastrados',name='listarcarros'),

    url(r'^home/estacionamento/cliente/$','registros.views.viewCadastroCliente',name='cliente'),
    url(r'^home/estacionamento/cliente/editarcliente/(?P<id>[0-9]+)/$','registros.views.viewCadastroCliente',name='editarcliente'),
    url(r'^home/estacionamento/listarclientes/$','registros.views.inserirClientesCadastrados',name='listarclientes'),

    url(r'^home/estacionamento/criarVaga/$','registros.views.viewCriarVaga',name='vaga'),
    url(r'^home/estacionamento/criarVaga/editarvaga/(?P<id>[0-9]+)/$','registros.views.viewCriarVaga',name='editarvaga'),
    url(r'^home/estacionamento/listarVaga/$','registros.views.inserirVagasCadastradas',name='listarvagas'),

    url(r'^home/estacionamento/reserva/$','registros.views.viewCriarReserva',name='reserva'),
     url(r'^home/estacionamento/reserva/editarreserva/(?P<id>[0-9]+)/$','registros.views.viewCriarReserva',name='editarreserva'),
    url(r'^home/estacionamento/listarreservas/$','registros.views.inserirReserva',name='listarreservas'),
    

] 


