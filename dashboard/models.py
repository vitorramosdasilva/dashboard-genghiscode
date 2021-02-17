from django.db import models
from django.conf import settings


class Operacao(models.Model):
    nome_operacao = models.CharField(max_length=150)
    descricao = models.CharField(max_length=250)
    data_criacao = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    class Meta:
        db_table = "operacao"

    def __str__(self):
        return self.nome_operacao


class TipoCampanha(models.Model):
    tipoCampanha = models.CharField(max_length=50)

    class Meta:
        db_table = "tipocampanha"

    def __str__(self):
        return self.tipoCampanha


class Campanha(models.Model):
    nome_campanha = models.CharField(max_length=150)
    descricao = models.CharField(max_length=250)
    data_criacao = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    operacao = models.ForeignKey(Operacao, on_delete=models.CASCADE)
    tipoCampanha = models.ForeignKey(TipoCampanha, on_delete=models.CASCADE)

    class Meta:
        db_table = "campanha"

    def __str__(self):
        return self.nome_campanha


class Discagem(models.Model):
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE)
    data = models.DateField()
    classificacao = models.CharField(max_length=150)
    tabulacao = models.CharField(max_length=200)
    faixa = models.CharField(max_length=200)
    unic = models.IntegerField()
    tentativas = models.IntegerField()

    class Meta:
        db_table = "discagem"

    def __str__(self):
        return self.campanha.nome_campanha


class Tempo(models.Model):
    id_campanha = models.IntegerField()
    campanha = models.CharField(max_length=150)
    data = models.DateField()
    login = models.IntegerField()
    status = models.CharField(max_length=100)
    tempo = models.IntegerField()

    class Meta:
        db_table = "tempo"

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

    class Meta:
        db_table = "mailing"

    def __str__(self):
        return self.mailing


class Carteira(models.Model):
    id_carteira = models.IntegerField()
    dt_referencia = models.DateField()
    nr_conta = models.IntegerField()
    carteira = models.CharField(max_length=200)
    faixa = models.CharField(max_length=200)
    qtd_carteira = models.IntegerField()
    vl_carteira = models.DecimalField(max_digits=18, decimal_places=2)
    qtd_pagamentos = models.IntegerField()
    vl_pago = models.DecimalField(max_digits=18, decimal_places=2)
    qtd_pag_acordo = models.IntegerField()
    pagamento_acordo = models.DecimalField(max_digits=18, decimal_places=2)
    qtd_colchao = models.IntegerField()
    PagamentoColchao = models.DecimalField(max_digits=18, decimal_places=2)
    qtd_espontaneo = models.IntegerField()
    pagamento_espontaneo = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        db_table = "carteira"

    def __str__(self):
        return self.carteira
