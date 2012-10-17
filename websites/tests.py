# -*- coding: utf-8 -*-

import os

from django.core.urlresolvers import reverse
from django.test import TestCase, TransactionTestCase

from django.contrib.auth.models import User

from models import Website


class WebsiteFixtures(object):
    def get_config(self):
        return dict(
            title="Prswb",
            url="http://prswb.fr",
            description="Scrum vu des petites tranchees.",
            request_type=Website.REQUEST_COMMENT)

    def generate_websites(self):
        return Website.objects.create(**self.get_config())


class WebsiteModelTest(TestCase, WebsiteFixtures):
    pass


class ViewListTest(TestCase, WebsiteFixtures):
    def setUp(self):
        self.website = self.generate_websites()

    def test_displays_website(self):
        response = self.client.get('/fr/sites-proposes/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.website.url, response.content)
        self.assertIn(self.website.title, response.content)


class SubmitWebsiteTest(TransactionTestCase, WebsiteFixtures):
    def setUp(self):
        self.user = User.objects.create(username='jdoe')
        self.user.set_password('jdoepswd')
        self.user.save()

    def test_suggest_website_unauthenticated(self):
        response = self.client.get(reverse('suggest_website'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_suggest_website_authenticated(self):
        self.client.login(username='jdoe', password='jdoepswd')
        response = self.client.get(reverse('suggest_website'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websites/suggest.html')
        with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'green-nature.jpg')) as fp:
            website_data = self.get_config()
            website_data.update(picture=fp)
            response = self.client.post(reverse('suggest_website'), website_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'websites/index.html')
        self.assertIn("http://prswb.fr", response.content)


class UtilsTest(TestCase):
    def test_url_informations(self):
        pass
