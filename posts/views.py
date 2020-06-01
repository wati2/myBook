from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

<<<<<<< HEAD
def index(request):
    # 템플릿 호출 
    template = loader.get_template('posts/index.html')

    # 딕셔너리 선언
    context ={}

    # 리스트 선언 (게시글: posts)
    posts = []
    # context에 dictionary 키, 밸류 추가
    context['posts'] = posts

    # 리스트 선언 (댓글전체)
    # 댓글은 DB에서 가져올 때 두개로 오름차순 해야함 , 1순위 commentsOrder 후, 그 다음 2순위 commentsInOrder
    
    replys = []
    # context에 dictionary 키, 밸류 추가
    context['replys'] = replys

    return HttpResponse(template.render(context,request))


=======
# Create your views here.

def index(request):
    return HttpResponse("hello")
>>>>>>> JISEONGDEV
