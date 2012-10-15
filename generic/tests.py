# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.test import TransactionTestCase

from django.contrib.auth.models import User


class RegistrationTest(TransactionTestCase):
    "Registration tests."

    def test_register(self):
        self.assertEquals(User.objects.filter(username='johndoe').count(), 0)
        response = self.client.get(reverse('registration_register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration_form.html')
        self.client.post(reverse('registration_register'), {
            'username':  'johndoe',
            'email':     'john@doe.org',
            'password1': 'doepsswd',
            'password2': 'doepsswd',
        }, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.filter(username='johndoe').count(), 1)
