from django.contrib import admin
from xadmin.layout import Row, Fieldset
from .models import Post, Tag, Category, Link, Comment, SideBar

# Register your models here.


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
    # 标签管理
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')
    list_filter = ('status', 'created_time')


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # 分类管理

    # 列表状态显示的字段
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'post_count')

    # 编辑页面上显示的字段
    fields = ('name', 'status', 'is_nav')

    # 列表状态过滤器用来筛选的字段
    list_filter = ('status', 'created_time')

    def post_count(self, obj):
        # 统计分类下文章数量
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    """友链"""
    list_display = ('title', 'weight', 'href', 'status', 'owner', 'created_time')
    fields = ('title', 'weight', 'href')
    list_filter = ('status', 'created_time')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
class PostAdmin(BaseOwnerAdmin):
    # 文章后台管理界面
    exclude = ('owner', )
    list_display = ('title', 'category', 'desc',  'status', 'created_time', 'owner', 'pv', 'uv')

    # fields = (('title', 'category', 'status'), 'desc', 'content', 'tag')

    form_layout = {
        Fieldset(
            '基础信息',
            Row("title", "category"),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    }
    # fieldsets = (
    #     ('基础配置', {
    #         'description': '基础配置描述',
    #         'fields': (('title', 'category'), 'status',),
    #     }),
    #     ('内容', {
    #         'fields': ('content', 'desc',),
    #     }),
    #     ('额外信息', {
    #         'classes': ('collapse',),
    #         'fields': ('tag',),
    #     })
    # )

    list_filter = ('category', 'created_time')

    search_fields = ('title', 'category__name')

    list_display_links = []

    # 动作相关显示位置
    actions_on_top = True
    actions_on_bottom = True

    # 编辑保存显示位置
    save_on_top = True
    save_on_bottom = True

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    """评论"""
    list_display = ('target', 'content', 'nickname', 'website', 'email', 'status', 'created_time')
    fields = ('target', 'content', 'nickname', 'website', 'email')
    list_filter = ('status', 'created_time')


@admin.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    """侧边栏"""
    list_display = ('title', 'display_type', 'content', 'status', 'owner', 'created_time')
    fields = ('title', 'display_type', 'content')
    list_filter = ('status', 'created_time')
