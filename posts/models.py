from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField()
    view_count = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    image = models.ImageField(upload_to='images/', null=True)
    # upload_to는 media 폴더 안에 images 라는 폴더로 들어가라는 의미이다.
    # files = models.FileField(upload_to='files/', null=True)

    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)