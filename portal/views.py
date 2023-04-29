from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request, 'portal/home.html')
