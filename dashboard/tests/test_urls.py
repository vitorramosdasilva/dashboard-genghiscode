from django.test import TestCase
import pytest
from django.urls import reverse, resolve
from my_proj import urls
from django.test.client import RequestFactory
from dashboard.views import IndexView, funcao_total_alo, SobreView, funcao_total_cpc, funcao_total_acordo, \
    funcao_acordo_cpc, funcao_acordo_alo, discagem_tentativas, discagem_unicas, discagem_acordos, discagem_classificacao_unicas, \
    discagem_maquinas_unic, error_400, error_50x, error_403, error_404


class TestUrls(TestCase):

    def test_index_url_is_resolved(self):
        url = reverse('dashboard:index')
        # print(url)
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_sobre_url_is_resolved(self):
        url = reverse('dashboard:sobre')
        # print(url)
        self.assertEquals(resolve(url).func.view_class, SobreView)

    def test_total_alo_url_is_resolved(self):
        url = reverse('dashboard:total-alo')
        # print(url)
        self.assertEquals(resolve(url).func, funcao_total_alo)

    def test_total_cpc_url_is_resolved(self):
        url = reverse('dashboard:total-cpc')
        # print(url)
        self.assertEquals(resolve(url).func, funcao_total_cpc)

    def test_total_acordo_url_is_resolved(self):
        url = reverse('dashboard:total-acordo')
        # print(url)
        self.assertEquals(resolve(url).func, funcao_total_acordo)

    def test_acordo_cpc_url_is_resolved(self):
        url = reverse('dashboard:acordo_cpc')
        # print(url)
        self.assertEquals(resolve(url).func, funcao_acordo_cpc)

    def test_acordo_alo_url_is_resolved(self):
        url = reverse('dashboard:acordo_alo')
        # print(url)
        self.assertEquals(resolve(url).func, funcao_acordo_alo)

    def test_discagem_tentativas_url_is_resolved(self):
        url = reverse('dashboard:discagem-tentativas')
        # print(url)
        self.assertEquals(resolve(url).func, discagem_tentativas)

    def test_discagem_unicas_url_is_resolved(self):
        url = reverse('dashboard:discagem-unicas')
        # print(url)
        self.assertEquals(resolve(url).func, discagem_unicas)

    def test_discagem_acordos_url_is_resolved(self):
        url = reverse('dashboard:discagem-acordos')
        # print(url)
        self.assertEquals(resolve(url).func, discagem_acordos)

    def test_discagem_classificacao_unicas_url_is_resolved(self):
        url = reverse('dashboard:classificacao-unicas')
        # print(url)
        self.assertEquals(resolve(url).func, discagem_classificacao_unicas)

    def test_discagem_maquinas_unic_url_is_resolved(self):
        url = reverse('dashboard:discagem-maquinas-unic')
        # print(url)
        self.assertEquals(resolve(url).func, discagem_maquinas_unic)


