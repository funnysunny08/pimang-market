from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name="유저이름")
    age = models.IntegerField(default=0, verbose_name="유저나이")
    

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    region = models.CharField(max_length=50, verbose_name="지역")
    price = models.IntegerField(verbose_name="가격")
    content = models.TextField(verbose_name="컨텐츠")
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name="사진")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    