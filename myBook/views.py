from django.shortcuts import render
from django.http import HttpResponse 
from . import make_json
def index(request):
    all_data = make_json.make_json_data()
    print (all_data)
    return HttpResponse(all_data)
