from django.contrib import admin
from .models import Post, Tag


class BaseOwnerAdmin(admin.ModelAdmin):
    # class BaseOwnerAdmin:     # 使用xadmin，将admin.ModelAdmin去掉
    """
    1、自动补充文章、分类、标签、侧边栏、友链这些Model的owner字段
    2、用来针对get_queryset过滤当前用户的数据
    """
    exclude = ('owner', )

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('tag', 'owner')
    fields = ('tag', )
    list_filter = ('tag', 'owner')
    pass


@admin.register(Post)
class PostAdmin(BaseOwnerAdmin):
    list_display = ('title', 'content', 'owner', 'create_time')
    fields = ('title', 'content', 'tag')
    list_filter = ('title', )
    pass
