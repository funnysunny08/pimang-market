from dataclasses import field
from django.contrib import admin
from .models import Post, User
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'content', 'price', 'region', 'photo')
        export_order = fields

class PostAdmin(ImportExportModelAdmin):
    fields = ('title', 'user', 'content', 'price', 'region', 'photo')
    list_display = ('id', 'title', 'user', 'content', 'price', 'region', 'photo')
    resource_class = PostResource

admin.site.register(Post, PostAdmin)