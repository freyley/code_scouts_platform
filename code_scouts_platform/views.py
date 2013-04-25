# -*- coding: utf-8 -*-
"""Project-level views for the Code Scouts Platform."""
import logging
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render
from django.utils.http import is_safe_url

logger = logging.getLogger(__name__)

def login(request):
    redirect_to = request.REQUEST.get(REDIRECT_FIELD_NAME, '')
    # Ack, don't leave an open redirect.
    # https://github.com/omab/django-social-auth/issues/676
    if not is_safe_url(redirect_to, request.get_host()):
        logger.warning(
            "Suspect redirect URL provided to login: %r" % (redirect_to,),
            extra={request: request})
        redirect_to = ''
    return render(request, 'code_scouts_platform/login.html', {
        'redirect_to': redirect_to,
        'REDIRECT_FIELD_NAME': REDIRECT_FIELD_NAME,
    })
