from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    # 템플릿 호출 
    template = loader.get_template('posts/index.html')

    # 딕셔너리 선언
    context ={}

    # 리스트 선언
    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("second entry")
    list_of_values.append("third entry")
    list_of_values.append("fourth entry")
    # context에 dictionary 키, 밸류 추가
    context['list_of_values'] = list_of_values


    # 리스트 선언 (게시글: posts)
    posts = []
    posts.append({'postId':1, 'userId':'wati2', 'contents':'Cupidatat labore eu mollit est.', 'date':'', 'like':'100000'})
    posts.append({'postId':2, 'userId':'ajrqhxn', 'contents':'Voluptate amet cupidatat fugiat laboris ut.', 'date':'', 'like':'2'})
    posts.append({'postId':3, 'userId':'iqjumps', 'contents':'Mollit anim ex elit in quis aliqua officia sint dolore elit nisi veniam.', 'date':'', 'like':'3'})
    posts.append({'postId':4, 'userId':'hyeripang', 'contents':'Officia nostrud sunt ipsum qui nulla in adipisicing aliqua ut laborum.', 'date':'', 'like':'0'})
    # context에 dictionary 키, 밸류 추가
    context['posts'] = posts

    # 리스트 선언 (댓글전체)
    # 댓글은 DB에서 가져올 때 두개로 오름차순 해야함 , 1순위 commentsOrder 후, 그 다음 2순위 commentsInOrder
    replys = []
    replys.append({'replyId':1,'postId':1, 'commentsOrder':1, 'commentsInOrder':0, 'contents':'맛있다', 'time':'12:01', 'userId':'wati2'})
    replys.append({'replyId':4,'postId':1, 'commentsOrder':1, 'commentsInOrder':1, 'contents':'혼자먹냐?', 'time':'12:04', 'userId':'hyeripang'})
    replys.append({'replyId':5,'postId':1, 'commentsOrder':1, 'commentsInOrder':2, 'contents':'담에ㄱ?', 'time':'12:05', 'userId':'wati2'})
    replys.append({'replyId':2,'postId':1, 'commentsOrder':2, 'commentsInOrder':0, 'contents':'양ㄷㄷ', 'time':'12:02', 'userId':'iqjumps'})
    replys.append({'replyId':3,'postId':1, 'commentsOrder':3, 'commentsInOrder':0, 'contents':'비주얼ㄷㄷ', 'time':'12:03', 'userId':'ajrqhxn'})
    # context에 dictionary 키, 밸류 추가
    context['replys'] = replys

    # print(context)

    return HttpResponse(template.render(context,request))


