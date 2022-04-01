from re import T
from django.db import models

class Board(models.Model):
    tag = models.CharField(max_length=30, verbose_name='게시글 종류')
    title = models.CharField(max_length=60, verbose_name='제목')
    content = models.TextField(blank=True, verbose_name='내용') 
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    view_cnt = models.IntegerField(default=0, verbose_name='조회수')
    e_start = models.DateField(null=True, verbose_name='이벤트 시작일')
    e_end = models.DateField(null=True, verbose_name='이벤트 종료일')

    class Meta:
        db_table = 't_board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글(들)'

    def __str__(self):
        return self.title