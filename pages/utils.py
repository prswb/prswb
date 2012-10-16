import os

from django.conf import settings


def resolve_markdown_path(slug, lang=None):
    """ Retrieves an existing markdown file path from slug and a language code.
        Returns None in case no matching file was found.
    """
    if lang is None:
        return slug
    i18n_filename = os.path.join(settings.MARKDOWN_DIR, lang, '%s.md' % slug)
    filename = os.path.join(settings.MARKDOWN_DIR, '%s.md' % slug)
    if os.path.isfile(i18n_filename):
        return i18n_filename
    elif os.path.isfile(filename):
        return filename
