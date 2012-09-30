"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class SimpleTest(TestCase):
    
    def setUp(self):
        self.Client = Client()

    def tearDown(self):
        del self.Client

    def test_user_creation(self):
        """
        Tests user creation
        Response is redirected
        """
        datas = {"username": "test", "email": "plop@plop.com", 
                "password1": "apassbutnotword", "password2": "apassbutnotword"}
        response = self.Client.post("/compte/creation/", datas)
        print(response)
        self.assertRedirects(response, "/compte/creation/merci/")
