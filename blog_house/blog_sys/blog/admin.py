from django.contrib import admin
from .models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'name',
#                 ('status', 'is_nav'),
#                 ('owner'),
#             )
#         }),
#     )
#
#
# admin.site.register(Category, CategoryAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'name',
#                 ('status', 'owner'),
#             )
#         }),
#     )
#
#
# admin.site.register(Tag, TagAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'content', 'status', 'category',
                    'owner', 'created_time')
    list_filter = ('status', 'created_time')
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'title',
#                 ('desc', 'content', 'category'),
#                 ('status', 'owner'),
#             )
#         }),
#     )
#
#
# admin.site.register(Post, PostAdmin)
