from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    user = models.CharField(max_length=50, verbose_name="유저")
    region = models.CharField(max_length=50, verbose_name="지역")
    price = models.IntegerField(verbose_name="가격")
    content = models.TextField(verbose_name="컨텐츠")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    