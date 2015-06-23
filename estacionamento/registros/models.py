#coding:utf-8
from django.db import models
from django.core.exceptions import ValidationError
import datetime 
from django.utils import timezone
# Create your models here.

SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')

]


class cliente(models.Model):
	
	Nome = models.CharField('Nome',max_length=25,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=15,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Endereço de email',max_length=100)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	Limite = models.IntegerField('Limite de Vagas',default=1)
 	def __unicode__(self):
		return self.Nome
	class Meta:
		verbose_name = "Cadastro de Cliente" 
		verbose_name_plural = "Cadastro de Clientes"


class carro(models.Model):
	Marca = models.CharField('Marca',max_length=100,null=True)
	Modelo = models.CharField('Modelo',max_length=100,null=True)
	Placa = models.CharField('Placa',max_length=7,null=True)
	Cor = models.CharField('Cor',max_length=20,null=True)
	Ano = models.IntegerField('Ano Fabricação', null=True)
	def __unicode__(self):
		return u"%s - %s - %s"%(self.Marca,self.Modelo,self.Placa)
	class Meta:
		verbose_name = "Cadastro de Carro"
		verbose_name_plural = "Cadastro de Carros"

		
class vaga(models.Model):
	NomeVaga = models.CharField('Vaga',max_length=100, null=True)
	def __unicode__(self):
		return self.NomeVaga
	class Meta:
		verbose_name = "Cadastro de Vaga"
		verbose_name_plural = "Cadastro de Vagas"


class alugarvaga (models.Model):

	cliente = models.ForeignKey(cliente,verbose_name="cliente",null=True)
	carro = models.ForeignKey(carro,verbose_name="carro",null=True)
	vaga = models.ForeignKey(vaga,verbose_name="vaga",null=True)
	tempoentrada = models.TimeField('Entrada',null=True)
	temposaida = models.TimeField('Saida',blank=True,null=True)

	def __unicode__(self):
		return u"%s - %s - %s"%(self.cliente.Nome,self.carro,self.vaga)

	class Meta:
		verbose_name = "Alugar Vaga"
		verbose_name_plural = "Alugar Vagas"







