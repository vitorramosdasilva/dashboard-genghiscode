from django.test import TestCase
import pytest
from django.urls import reverse, resolve
from my_proj import urls
from django.test.client import RequestFactory
from dashboard.views import IndexView, funcao_total_alo, SobreView, funcao_total_cpc, funcao_total_acordo, \
    funcao_acordo_cpc, funcao_acordo_alo, discagem_tentativas, \
    discagem_unicas, discagem_acordos, discagem_classificacao_unicas, discagem_maquinas_unic, \
    error_400, error_50x, error_403, error_404


class TestViews(TestCase):

    def test_index_status_sucess(self):
        response = self.client.get(reverse('dashboard:index'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_sobre_status_sucess(self):
        response = self.client.get(reverse('dashboard:sobre'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_total_alo_status_sucess(self):
        response = self.client.get(reverse('dashboard:total-alo'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_total_cpc_status_sucess(self):
        response = self.client.get(reverse('dashboard:total-cpc'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_total_acordo_status_sucess(self):
        response = self.client.get(reverse('dashboard:total-acordo'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_acordo_cpc_status_sucess(self):
        response = self.client.get(reverse('dashboard:acordo_cpc'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_acordo_alo_status_sucess(self):
        response = self.client.get(reverse('dashboard:acordo_alo'))  # for first object
        self.assertEquals(response.status_code, 200)

    def test_discagem_tentativas_status_sucess(self):
        response = self.client.get(reverse('dashboard:discagem-tentativas'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_discagem_unicas_status_sucess(self):
        response = self.client.get(reverse('dashboard:discagem-unicas'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_discagem_acordos_status_sucess(self):
        response = self.client.get(reverse('dashboard:discagem-acordos'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_discagem_classificacao_unicas_status_sucess(self):
        response = self.client.get(reverse('dashboard:classificacao-unicas'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_discagem_maquinas_unicas_status_sucess(self):
        response = self.client.get(reverse('dashboard:discagem-maquinas-unic'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_error_400(self):
        self.assertTrue(urls.handler404.endswith('.error_404'))
        factory = RequestFactory()
        request = factory.get('/')
        response = error_404(request, 404)
        # print('my response : ' + str(response))
        self.assertEqual(response.status_code, 404)

    def test_error_403(self):
        self.assertTrue(urls.handler403.endswith('.error_403'))
        factory = RequestFactory()
        request = factory.get('/')
        response = error_403(request, 403)
        # print('my response : ' + str(response))
        self.assertEqual(response.status_code, 403)

    def test_error_404(self):
        self.assertTrue(urls.handler404.endswith('.error_404'))
        factory = RequestFactory()
        request = factory.get('/')
        response = error_404(request, 404)
        # print('my response : ' + str(response))
        self.assertEqual(response.status_code, 404)

    def test_error_50x(self):
        self.assertTrue(urls.handler50x.endswith('.error_500'))
        factory = RequestFactory()
        request = factory.get('/')
        response = error_50x(request, 500)
        # print('my response : ' + str(response))
        self.assertEqual(response.status_code, 500)
