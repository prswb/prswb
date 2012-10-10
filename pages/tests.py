# -*- coding: utf-8 -*-
from os import path, remove

from django.test import TestCase
from django.conf import settings


class MarkdownPageTest(TestCase):

    def test_page_existence(self):
        """
        Tests that you can reach a page if the markdown file exists.
        """
        # if the page doesn't exist, we should have a 404
        response = self.client.get('/pages/this-page-doesnt-exist/')
        self.assertEqual(response.status_code, 404)

        # if the page exists, we should have rendered HTML
        response = self.client.get('/pages/mentions-legales/')
        self.assertTemplateUsed(response, 'pages/markdown.html')
        self.assertContains(response, "<h1> Mentions légales</h1>")

    def test_page_life(self):
        """
        Tests that you can create a page via a newly created markdown
        file and still raise a 404 on deletion.
        """
        # if the page doesn't exist, we should have a 404
        response = self.client.get('/pages/test-page/')
        self.assertEqual(response.status_code, 404)

        # let's create the page
        page_filepath = path.join(settings.MARKDOWN_DIR, 'test-page.md')
        with open(page_filepath, 'w') as markdown_file:
            markdown_file.write("# This is a test")

        # check the HTML dynamic rendering
        response = self.client.get('/pages/test-page/')
        self.assertContains(response, "<h1>This is a test</h1>")

        # finally remove the markdown file newly created
        remove(page_filepath)

        # if the file has been removed, we should get back to a 404
        response = self.client.get('/pages/test-page/')
        self.assertEqual(response.status_code, 404)

