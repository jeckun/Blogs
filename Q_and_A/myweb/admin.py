from django.contrib import admin
from myweb.models import Answer, Questions

# Register your models here.


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'status', 'datetime', 'thumbs_up', 'comments')
    fields = ('owner', 'title', 'content', 'status', 'thumbs_up', 'comments')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'question', 'content', 'datetime', 'ip_address')
    fields = ('owner', 'question', 'content', 'ip_address' )
