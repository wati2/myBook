from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):


    return redirect('/posts/')
