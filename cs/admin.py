from django.contrib import admin
from cs.models import Board
from cs.models import Inquire

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'title',)

admin.site.register(Board, BoardAdmin)

class InquireAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'answer',)

admin.site.register(Inquire, InquireAdmin)
