from django.contrib import admin
from .models import Link, SideBar


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight', 'href', 'status', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'title',
#                 ('href', 'weight', 'status', 'owner'),
#             )
#         }),
#     )
#
#
# admin.site.register(Link, LinkAdmin)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'status', 'owner', 'created_time')
    list_filter = ('status', 'created_time')
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'title',
    #             ('display_type', 'content', 'status', 'owner'),
    #         )
    #     }),
    # )


# admin.site.register(SideBar, SideBarAdmin)
