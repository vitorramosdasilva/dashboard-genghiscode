from django.test import TestCase
from dashboard.models import Discagem, Campanha, Operacao, TipoCampanha, Tempo, Mailing, Carteira
from django.shortcuts import get_object_or_404
from datetime import date
from model_mommy import mommy
from model_mommy.recipe import Recipe
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_Discagem(self):
        discagem = Campanha(nome_campanha="Test Campanha")
        self.assertEqual(str(discagem), discagem.nome_campanha)

    def test_Operacao(self):
        operacao = Operacao(nome_operacao="Test Campanha")
        self.assertEqual(str(operacao), operacao.nome_operacao)

    def test_tipoCampanha(self):
        tipoCampanha = TipoCampanha(tipoCampanha="Test Campanha")
        self.assertEqual(str(tipoCampanha), tipoCampanha.tipoCampanha)

    def test_campanha(self):
        campanha = Campanha(nome_campanha="Test Campanha")
        self.assertEqual(str(campanha), campanha.nome_campanha)

    def test_tempo(self):
        tempo = Tempo(campanha="Test Campanha")
        self.assertEqual(str(tempo), tempo.campanha)

    def test_mailing(self):
        mailing = Mailing(mailing="Test Campanha")
        self.assertEqual(str(mailing), mailing.mailing)

    def test_carteira(self):
        carteira = Carteira(carteira="Test Campanha")
        self.assertEqual(str(carteira), carteira.carteira)

    def test_object_TipoCampanha(self):
        myObj = mommy.make('dashboard.TipoCampanha', _quantity=3)
        assert len(myObj) == 3

    def test_object_Tempo(self):
        myObj = mommy.make('dashboard.Tempo', _quantity=3)
        assert len(myObj) == 3

    def test_object_Mailing(self):
        myObj = mommy.make('dashboard.Mailing', _quantity=3)
        assert len(myObj) == 3

    def test_object_Carteira(self):
        myObj = mommy.make('dashboard.Carteira', _quantity=3)
        assert len(myObj) == 3

    def test_object_Operacao(self):
        operacao = mommy.make('dashboard.Operacao', _quantity=3)
        assert len(operacao) == 3

    def test_object_Campanha(self):
        campanha = mommy.make('dashboard.Campanha', _quantity=3)
        assert len(campanha) == 3

    def test_object_Discagem(self):
        discagem = mommy.make('dashboard.Discagem', _quantity=3)
        assert len(discagem) == 3






