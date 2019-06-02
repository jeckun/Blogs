from django.contrib import admin
from .models import Link, SideBar


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'href', 'status', 'owner', 'created_time')
    fields = ('title', 'weight', 'href')
    list_filter = ('status', 'created_time')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'status', 'owner', 'created_time')
    fields = ('title', 'display_type', 'content')
    list_filter = ('status', 'created_time')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)