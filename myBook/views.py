<<<<<<< HEAD
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):


    return redirect('/posts/')
=======
from django.shortcuts import render
from django.http import HttpResponse 
from . import make_json
def index(request):
    # all_data = make_json.make_json_data()
    # print (all_data)
    # return HttpResponse(all_data)
>>>>>>> JISEONGDEV
