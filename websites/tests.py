# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from django.conf import settings

from models import Website
import utils

import os


class WebsiteFixtures(object):
    def get_config(self):
        return dict(
            title="Prswb",
            url="http://prswb.fr",
            description="Scrum vu des petites tranchees.",
            request_type=Website.REQUEST_COMMENT,
            picture=os.path.join(
                os.path.dirname(__file__), 'fixtures', 'green-nature.jpg'
                )
            )
    def generate_websites(self):
        return Website.objects.create(**self.get_config())


class WebsiteModelTest(TestCase, WebsiteFixtures):
    pass


class ViewListTest(TestCase, WebsiteFixtures):
    def setUp(self):
        self.client = Client()
        self.website = self.generate_websites()

    def test_displays_website(self):
        response = self.client.get('/sites-proposes/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.website.url, response.content)
        self.assertIn(self.website.title, response.content)

class SubmitWebsiteTest(TestCase, WebsiteFixtures):
    def setUp(self):
        self.client = Client()
    def test_suggest_website(self):
        response = self.client.post('/proposer-un-site/', self.get_config())
        # FIXME : client.post() has no way to post a file
        #self.assertEqual(response.status_code, 302)
        #response = self.client.get('/sites-proposes/')
        #self.assertIn("http://prswb.fr", response.content)

class UtilsTest(TestCase):
    def test_url_informations(self):
        pass
        #self.assertEqual(utils.get_url_informations("http://prswb.fr"), [])
