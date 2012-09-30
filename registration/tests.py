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
        self.registred = User.objects.get(id=1)
        self.Client = Client()

    def test_user_creation(self):
        """
        Tests user creation
        Response is redirected and new user is in database.
        """
        datas = {"username": "test", "email": "plop@plop.com", 
                "password1": "apassbutnotword", }
        response = self.Client.post("/compte/creation/", datas)
        print(response)
        self.assertRedirects(response, "/compte/merci/")
