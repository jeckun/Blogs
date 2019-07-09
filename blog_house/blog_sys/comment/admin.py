from django.contrib import admin
from .models import Comment

from blog.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    """评论"""
    list_display = ('target', 'content', 'nickname', 'website', 'email', 'status', 'created_time')
    fields = ('target', 'content', 'nikename', 'website', 'email')
    list_filter = ('status', 'created_time')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CommentAdmin, self).save_model(request, obj, form, change)
