from django.contrib import admin
from .models import Link, SideBar


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'href', 'status', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                ('href', 'weight', 'status'),
                ('owner', 'created_time'),
            )
        }),
    )


admin.site.register(Link, LinkAdmin)


class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'status', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
    fieldsets = (
        (None, {
            'fields': (
                'title',
                ('display_type', 'content', 'status'),
                ('owner', 'created_time'),
            )
        }),
    )


admin.site.register(SideBar, SideBarAdmin)
