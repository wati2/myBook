from posts.models import post_table, user_table, comment_table
from django.http import JsonResponse #장고에서 json 형식 사용할때 필요

def make_json_data():
     #포스트, 댓글용 딕셔너리

    all_dicData = {}
    postList = []
    subDict = {}
    commentList = []

    post_data = post_table.objects.all()
    
    p_idx = 0 #포스트 인덱스
    for p_data in post_data : #모든 포스트만큼 반복
        p_idx = p_idx + 1
        
        
        subDict['postId'] = p_data.id
        subDict['owner'] = p_data.owner
        subDict['date'] = p_data.make_date
        subDict['like'] = p_data.like_count
        subDict['content'] = p_data.content
        
        postList.append(subDict)

        #변수 초기화
        subDict = {}

    
        #포스트번호에 해당하는 댓글들 딕셔너리로 만들기
    
    #comment_data = comment_table.objects.filter(post_id = p_data.id)
    c_idx = 0#댓글 인덱스
    comment_data = comment_table.objects.all()
    for c_data in comment_data : 
        c_idx = c_idx + 1
        subDict['replyId'] = c_data.id
        subDict['commentsOrder'] = c_data.num
        subDict['commentsInOrder'] = c_data.num_sub
        subDict['date'] = c_data.make_date
        subDict['content'] = c_data.comment_data
        subDict['userId'] = c_data.comment_owner
        commentList.append(subDict)
        subDict = {}

    all_dicData['post'] = postList
    all_dicData['replys'] = commentList
    # return JsonResponse(postDict)
    return all_dicData