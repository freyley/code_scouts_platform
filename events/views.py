# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

def CalendarView(request):
	# return HttpResponse("Test Calendar View")
	return render(request, 'events/calendar.html')
