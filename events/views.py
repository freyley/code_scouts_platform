# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings

def calendar_view(request):
    return render(request, 'events/calendar.html', {
        'calendar_id': settings.CS_GOOGLE_CALENDAR
    })
