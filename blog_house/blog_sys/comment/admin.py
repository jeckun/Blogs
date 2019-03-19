from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'content', 'nickname', 'website', 'email', 'status', 'created_time')
    list_filter = ('status', 'created_time')
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'target',
    #             ('content', 'nickname', 'website', 'email', 'status'),
    #         )
    #     }),
    # )


# admin.site.register(Comment, CommentAdmin)
