from django.db import models

class Discagem(models.Model):
    id_campanha = models.IntegerField()
    campanha = models.CharField(max_length=150)
    data = models.DateField()
    classificacao = models.CharField(max_length=150)
    tabulacao = models.CharField(max_length=200)
    faixa = models.CharField(max_length=200)	
    unic = models.IntegerField()
    tentativas = models.IntegerField()

    def __str__(self):
        return self.campanha


class Tempo(models.Model):
    id_campanha = models.IntegerField()
    campanha = models.CharField(max_length=150)
    data = models.DateField()
    login = models.IntegerField()
    status = models.CharField(max_length=100)
    tempo = models.IntegerField()
    
    def __str__(self):
        return self.campanha
        

class Mailing(models.Model):
    id_campanha = models.IntegerField()    
    mailing = models.CharField(max_length=200)
    data = models.DateField()
    recebido = models.IntegerField()
    importado = models.IntegerField()
    trabalhado = models.IntegerField()
    campanha = models.CharField(max_length=150)

    def __str__(self):
        return self.mailing


class Carteira(models.Model):
    id_carteira = models.IntegerField()
    dt_referencia = models.DateField()
    nr_conta = models.IntegerField()
    carteira = models.CharField(max_length=200)
    faixa = models.CharField(max_length=200)
    qtd_carteira = models.IntegerField()
    vl_carteira	= models.DecimalField(max_digits=18, decimal_places=2)
    qtd_pagamentos = models.IntegerField()
    vl_pago	= models.DecimalField(max_digits=18, decimal_places=2)
    qtd_pag_acordo	= models.IntegerField()
    pagamento_acordo = models.DecimalField(max_digits=18, decimal_places=2)
    qtd_colchao	= models.IntegerField()
    PagamentoColchao = models.DecimalField(max_digits=18, decimal_places=2)	
    qtd_espontaneo = models.IntegerField()
    pagamento_espontaneo = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return self.carteira
   