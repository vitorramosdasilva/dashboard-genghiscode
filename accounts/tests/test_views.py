from django.test import TestCase
import pytest
from django.urls import reverse, resolve
from accounts import urls
from django.test.client import RequestFactory
from accounts.views import user_login, register
from accounts.forms import LoginForm, UserRegistrationForm


class TestViews(TestCase):

    # def setUp(self):
    #     self.user = User.objects.create(username="testautomatico", email="testautomatico@testautomatico.com.br", password="12345", password2="12345")

    def test_user_register_status_sucess(self):
        response = self.client.get(reverse('register'))  # for first object
        self.assertEqual(response.status_code, 200)

    def test_user_login_status_sucess(self):
        response = self.client.get(reverse('login'))  # for first object
        self.assertEqual(response.status_code, 200)

    def teste_user_login(self):
        form = LoginForm(data={"username": "teste@teste.com.br", "password": "12345"})
        self.assertTrue(form.is_valid())

    def test_register(self):
        form = UserRegistrationForm(data={"username": "testautomatico", "email": "testautomatico@testautomatico.com.br", "password": "12345", "password2": "12345"})
        self.assertTrue(form.is_valid())


