from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User


def home(request):
	page_title = "Como ayudar"	
	user = request.user
	return render(request, 'ong/index.html', locals())