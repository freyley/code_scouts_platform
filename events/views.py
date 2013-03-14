# -*- coding: utf-8 -*-

from django.shortcuts import render


def CalendarView(request):
    return render(request, 'events/calendar.html')
