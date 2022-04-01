from django.contrib import admin
from cs.models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'title',)

admin.site.register(Board, BoardAdmin)
