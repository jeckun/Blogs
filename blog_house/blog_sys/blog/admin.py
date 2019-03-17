from django.contrib import admin
from .models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('status', 'is_nav'),
                ('owner', 'create_time'),
            )
        }),
    )


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('status', 'owner', 'create_time'),
            )
        }),
    )


admin.site.register(Tag, TagAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'content', 'status', 'category',
                    'owner', 'created_time')
    list_filter = ('status', 'created_time')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                ('desc', 'content', 'category'),
                ('status', 'owner', 'create_time'),
            )
        }),
    )


admin.site.register(Post, PostAdmin)
