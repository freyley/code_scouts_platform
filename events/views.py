# -*- coding: utf-8 -*-

from django.http import HttpResponse

def CalendarView(request):
	return HttpResponse("Test Calendar View")

