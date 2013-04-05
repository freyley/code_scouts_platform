# -*- coding: utf-8 -*-
"""Project-level views for the Code Scouts Platform."""
from django.shortcuts import render


def login(request):
    return render(request, 'code_scouts_platform/login.html')
