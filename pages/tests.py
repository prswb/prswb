# -*- coding: utf-8 -*-

import os

from django.test import TestCase
from django.conf import settings
from django.core import mail


class MarkdownPageTest(TestCase):

    def test_page_existence(self):
        """
        Tests that you can reach a page if the markdown file exists.
        """
        # if the page doesn't exist, we should have a 404
        response = self.client.get('/fr/pages/this-page-doesnt-exist/')
        self.assertEqual(response.status_code, 404)

        # if the page exists, we should have rendered HTML
        response = self.client.get('/fr/pages/mentions-legales/')
        self.assertTemplateUsed(response, 'pages/markdown.html')
        self.assertContains(response, "<h1> Mentions légales</h1>")

    def test_page_life(self):
        """
        Tests that you can create a page via a newly created markdown
        file and still raise a 404 on deletion.
        """
        # root pages
        test_filepath = os.path.join(settings.MARKDOWN_DIR, 'test-page.md')
        if os.path.isfile(test_filepath):
            os.remove(test_filepath)
        # if the page doesn't exist, we should have a 404
        response = self.client.get('/fr/pages/test-page/')
        self.assertEqual(response.status_code, 404)

        # i18n mardown file
        with open(test_filepath, 'w') as markdown_file:
            markdown_file.write("Test page title\n\n# This is a test for all languages")

        # check the HTML dynamic rendering
        response = self.client.get('/fr/pages/test-page/')
        self.assertContains(response, "<title>UXperiment - Test page title</title>")
        self.assertContains(response, "<h1>This is a test for all languages</h1>")

        os.remove(test_filepath)

        # i18n pages
        for lang in [lng[0] for lng in settings.LANGUAGES]:
            # preliminary checks
            test_filepath = os.path.join(settings.MARKDOWN_DIR, lang,
                'test-page-%s.md' % lang)
            if os.path.isfile(test_filepath):
                os.remove(test_filepath)

            # if the page doesn't exist, we should have a 404
            response = self.client.get('/%s/pages/test-page-%s/' % (lang, lang,))
            self.assertEqual(response.status_code, 404)

            # i18n mardown file
            with open(test_filepath, 'w') as markdown_file:
                markdown_file.write("Title in %(lang)s\n\n# This is a test in %(lang)s"
                                    % dict(lang=lang))

            # check the HTML dynamic rendering
            response = self.client.get('/%s/pages/test-page-%s/' % (lang, lang,))
            self.assertContains(response, "<h1>This is a test in %s</h1>" % lang)

            # remove the test file
            os.remove(test_filepath)

            # if the file has been removed, we should get back to a 404
            response = self.client.get('/%s/pages/test-page-%s/' % (lang, lang,))
            self.assertEqual(response.status_code, 404)


class ContactPageTest(TestCase):

    def test_contact_submission(self):
        # first, we verify that the page exist
        response = self.client.get('/fr/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact")

        # then we submit the form and verify the redirection
        response = self.client.post('/fr/contact/', {
            "subject": "A test",
            "sender": "test@example.org",
            "message": "This website is wonderful!"
        })
        self.assertRedirects(response, '/fr/contact/merci/')

        # we verify that emails has been sent to the admin and the user
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].subject, 'Commentaire sur UXperiment')
        self.assertEqual(mail.outbox[1].subject, 'Nouveau contact sur UXperiment')
        self.assertEqual(mail.outbox[1].body,
            u'Email : test@example.org\nSujet : A test\nMessage :\nThis website is wonderful!')

    def test_bad_submission(self):
        # invalid subject
        response = self.client.post('/fr/contact/', {
            "subject": "",
            "sender": "test@example.org",
            "message": "This website is wonderful!"
        })
        self.assertFormError(response, 'form', 'subject',
            [u'Un sujet doit \xeatre renseign\xe9.'])

        response = self.client.post('/fr/contact/', {
            "subject": "fo",
            "sender": "test@example.org",
            "message": "This website is wonderful!"
        })
        self.assertFormError(response, 'form', 'subject',
            [u'3 caract\xe8res minimum sont requis.'])

        # invalid sender
        response = self.client.post('/fr/contact/', {
            "subject": "A test",
            "sender": "",
            "message": "This website is wonderful!"
        })
        self.assertFormError(response, 'form', 'sender',
            [u'Une adresse email est demand\xe9e.'])

        response = self.client.post('/fr/contact/', {
            "subject": "A test",
            "sender": "foo",
            "message": "This website is wonderful!"
        })
        self.assertFormError(response, 'form', 'sender',
            [u'Une adresse email valide doit \xeatre renseign\xe9e.'])

        # invalid message
        response = self.client.post('/fr/contact/', {
            "subject": "A test",
            "sender": "test@example.org",
            "message": ""
        })
        self.assertFormError(response, 'form', 'message',
            [u'Un message est demand\xe9.'])

        response = self.client.post('/fr/contact/', {
            "subject": "A test",
            "sender": "test@example.org",
            "message": "foobar"
        })
        self.assertFormError(response, 'form', 'message',
            [u'8 caract\xe8res minimum sont requis.'])
