# -*- coding: utf-8 -*-
"""Project-level views for the Code Scouts Platform."""
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render


def login(request):
    return render(request, 'code_scouts_platform/login.html', {
        'redirect_to': request.REQUEST.get(REDIRECT_FIELD_NAME, ''),
        'REDIRECT_FIELD_NAME': REDIRECT_FIELD_NAME,
    })
