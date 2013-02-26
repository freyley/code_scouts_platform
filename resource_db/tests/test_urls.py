# -*- coding: utf-8 -*-
"""Test resource_db.urls.
"""

from unittest import TestCase
from django.core.urlresolvers import resolve

from .. import urls
from .. import views


class TestURLs(TestCase):
    def test_resourceList(self):
        match = resolve('/', urls)
        self.assertEqual(match.func, views.ResourceList)
