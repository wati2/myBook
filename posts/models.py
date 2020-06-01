from django.db import models

# Create your models here.
class user_table(models.Model):
    #아이디, 비번, 친구목록
    user_id = models.CharField(max_length=20, unique = True)
    pw = models.CharField(max_length=20) 
    friend = models.TextField()

class post_table(models.Model):
    #포스트아이디, 글쓴이, 만든날, 좋아요, 내용
    def getContent(self):
        return self.content
        
    id = models.AutoField(primary_key=True)
    # owner = models.Foreignkey(user_table.id, on_delete=models.CASCADE)
    owner = models.CharField(max_length=20)
    make_date = models.DateTimeField(auto_now_add=True, blank=True)
    like_count=models.IntegerField(default=0)
    content = models.TextField()

class comment_table(models.Model):
    #코멘트아이디, 포스트아이디, 댓글쓴이, 코멘트순서, 대댓글순서, 댓글시간, 댓글내용
    id = models.AutoField(primary_key=True)
    post_id = models.IntegerField()
    comment_owner = models.CharField(max_length= 20)
    num = models.IntegerField()
    num_sub= models.IntegerField()
    make_date=models.DateField(auto_now=True)
    comment_data = models.TextField()
