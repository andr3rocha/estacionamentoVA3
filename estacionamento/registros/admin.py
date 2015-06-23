#coding:utf-8
from django.contrib import admin
from models import cliente,carro,vaga,alugarvaga
from datetime import datetime


# Register your models here.

class clienteAdmin(admin.ModelAdmin):
	list_display = ['Nome','CPF']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

class carroAdmin(admin.ModelAdmin):
	list_display = ['Marca','Modelo']
	list_filter = ['Marca']
	search_fields = ['Placa']
	save_as = True
	
class alugarvagaAdmin(admin.ModelAdmin):
	list_display = ['carro','cliente','vaga','tempoentrada','temposaida']
	list_filter = ['cliente','vaga']
	search_fields = ['carro','cliente','vaga']
	save_as = True

class vagaAdmin (admin.ModelAdmin):
	list_display = ['NomeVaga']
	list_filter = ['NomeVaga']
	search_fields = ['NomeVaga']
	save_as = True



admin.site.register(cliente,clienteAdmin)
admin.site.register(carro,carroAdmin)
admin.site.register(alugarvaga,alugarvagaAdmin)
admin.site.register(vaga,vagaAdmin) 