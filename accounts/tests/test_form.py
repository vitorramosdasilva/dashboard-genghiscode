from http import HTTPStatus
from django.test import TestCase


class LoginFormTests(TestCase):

    def test_login_form(self):
        response = self.client.post(
            "/accounts/login/", data={"username": "teste@teste.com.br", "password": "12345"}
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_UserRegistrationForm(self):
        response = self.client.post(
            "/accounts/register/", data={"username": "testautomatico",
                                         "email": "testautomatico@testautomatico.com.br",
                                         "password": "12345",
                                         "password2": "12345"
                                         }
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
