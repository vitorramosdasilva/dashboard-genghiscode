from django.test import TestCase
import pytest
from django.urls import reverse, resolve
from accounts import urls
from django.test.client import RequestFactory
from accounts.views import user_login, register


class TestUrls(TestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        # print(url)
        self.assertEquals(resolve(url).func, register)