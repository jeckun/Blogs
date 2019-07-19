from django.contrib import admin
from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ 添加后台Post管理 """
    list_display = ('title', 'desc', 'content', 'owner', 'create_time' )
    fields = ('title', 'desc', 'content', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    # 定义操作按钮
    actions_on_top = True
    actions_on_bottom = True

    # 保存操作按钮
    save_on_top = False
    # save_on_bottom = False