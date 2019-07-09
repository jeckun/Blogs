from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post
from .adminforms import PostAdminForm
from .custom_site import custom_site
from .base_admin import BaseOwnerAdmin


# class PostInline(admin.TabularInline):
class PostInline(admin.StackedInline):    # 换一种显示样式
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
# class CategoryAdmin(admin.ModelAdmin):
class CategoryAdmin(BaseOwnerAdmin):
    # 分类管理

    inlines = [PostInline, ]

    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    list_filter = ('status', 'created_time')

    # 已经在基类实现
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
# class TagAdmin(admin.ModelAdmin):
class TagAdmin(BaseOwnerAdmin):
    # 标签管理
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status')
    list_filter = ('status', 'created_time')

    # 基类已经实现
    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器：只显示当前用户 """
    title = "分类过滤器"
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
# class PostAdmin(admin.ModelAdmin):
class PostAdmin(BaseOwnerAdmin):
    # 文章管理

    # 引用自定义Form
    # 将文章的描述字段换为文本框
    form = PostAdminForm

    list_display = ('title', 'category', 'desc',  'status', 'created_time', 'owner', 'operator')

    exclude = ['owner', ]

    # fields = (('title', 'category', 'status'), 'desc', 'content', 'tag')
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (('title', 'category'), 'status',),
        }),
        ('内容', {
            'fields': ('content', 'desc',),
        }),
        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tag',),
        })
    )

    # list_filter = ('category', 'created_time')
    list_filter = [CategoryOwnerFilter]
    search_fields = ('title', 'category__name')

    list_display_links = []

    # 动作相关显示位置
    actions_on_top = True
    actions_on_bottom = True

    # 编辑保存显示位置
    save_on_top = True
    save_on_bottom = True

    # 已经在基类实现
    # def save_model(self, request, obj, form, change):
    #     """ 确保保存时候写入作者 """
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)

    # 已经在基类实现
    # def get_queryset(self, request):
    #     """ 查询时只看本人创建的 """
    #     qu = super(PostAdmin, self).get_queryset(request)
    #     return qu.filter(owner=request.user)

    def operator(self, obj):
        """ 点击编辑操作时直接打开对于页面进行编辑 """
        return format_html(
            '<a href="{}">编辑</a>',
            # reverse('admin:blog_post_change', args=(obj.id,))
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    class Media:
        # 定义静态资源
        css = {
            # 'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
        }
        # js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )
