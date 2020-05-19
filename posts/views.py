from django.http import HttpResponse
from django.template import loader

def index(request):
    # return HttpResponse("Hello, world. You're at the posts index.")
    template = loader.get_template('posts/index.html')
    return HttpResponse(template.render({'vPass':'전달된 값 헬로우'},request))

