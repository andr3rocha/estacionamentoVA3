#coding:utf-8
from django.forms import ModelForm
from models import cliente,carro,vaga,alugarvaga

class formCarro(ModelForm):
	class Meta:
		model=carro
		fields=['Marca','Modelo','Placa','Cor','Ano']


class formCliente(ModelForm):
	class Meta:
		model=cliente
		fields=['Nome','CPF','DataNascimento','Telefone','Celular','Email','Logradouro','Numero','Bairro','Cidade']

class formReserva(ModelForm):
	class Meta:
		model=alugarvaga
		fields=['cliente','carro','vaga','tempoentrada','temposaida']

class formVaga(ModelForm):
	class Meta:
		model=vaga
		fields=['NomeVaga'] 
 