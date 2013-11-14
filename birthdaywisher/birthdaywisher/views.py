__author__ = 'i813463'

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
	return render_to_response("index.html")
	#
	#return HttpResponse("Hello, you're inside login")