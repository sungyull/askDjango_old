# blog/asmin.py

from django.contrib import admin
from blog.models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','status', 'title', 'content_size', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    list_filter = ['created_at']

    actions = ['make_published', 'make_draft']

    def content_size(self, Post):
        return '{}글자'.format(len(Post.content))
        # return 'content글자수'

    def make_published (self, request, queryset ):
        update_cnt = queryset.update(status = 'p')
        self.message_user(request,
            '{}건의 포스팅을 P 상태로 변경했습니다.'.format(update_cnt))

    def make_draft (self, request, queryset ):
        update_cnt = queryset.update(status = 'd')
        self.message_user(request,
            '{}건의 포스팅을 D 상태로 변경했습니다.'.format(update_cnt))


    content_size.short_description = '본문글자수'
    make_published.short_description = '지정 포스팅을 퍼블리쉬 상태로 변경'
    make_draft.short_description = '지정 포스팅을 Draft 상태로 변경'

# admin.site.register(Post,PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','author','message','created_at', 'updated_at']
    list_display_links = ['post', 'message']
    list_filter = ['post','created_at']
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['name']




