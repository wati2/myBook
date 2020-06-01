from posts.models import post_table, user_table, comment_table
from django.http import JsonResponse #장고에서 json 형식 사용할때 필요

def make_json_data():
     #포스트, 댓글용 딕셔너리
    postDict = {}
    subDict = {}
    commentDict = {}
    subDict_comm2 = {}
    subDict_comm = {}

    post_data = post_table.objects.all()
    
    p_idx = 0 #포스트 인덱스
    for p_data in post_data : #모든 포스트만큼 반복
        p_idx = p_idx + 1
        c_idx = 0#댓글 인덱스
        
        subDict['id'] = p_data.id
        subDict['owner'] = p_data.owner
        subDict['make_date'] = p_data.make_date
        subDict['like_count'] = p_data.like_count
        subDict['content'] = p_data.content
        
        #포스트번호에 해당하는 댓글들 딕셔너리로 만들기
        comment_data = comment_table.objects.filter(post_id = p_data.id)
        for c_data in comment_data : 
            c_idx = c_idx + 1
            subDict_comm['comment_owner'] = c_data.comment_owner
            subDict_comm['num'] = c_data.num
            subDict_comm['num_sub'] = c_data.num_sub
            subDict_comm['make_date'] = c_data.make_date
            subDict_comm['comment_data'] = c_data.comment_data
            subDict_comm2['comment' + str(c_idx)] = subDict_comm
        
        subDict['comment'] = subDict_comm2

        postDict['post' + str(p_idx)] = subDict

        #변수 초기화
        subDict = {}
        subDict_comm = {}
        subDict_comm2 = {}

    return JsonResponse(postDict)