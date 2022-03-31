from django.db import models

# Create your models here.

class User(models.Model):
    # 관리자 여부
    admin = models.BooleanField(default=False, verbose_name="관리자모드")
    # 이메일
    email = models.EmailField(max_length=60, unique=True, verbose_name="이메일")
    # 비밀번호
    password = models.CharField(max_length=100, verbose_name="비밀번호")
    # 닉네임
    nickname = models.CharField(max_length=50, unique=True, verbose_name="닉네임")
    # 연락처
    contact = models.CharField(max_length=30, verbose_name="연락처")
    # 적립금
    point = models.IntegerField(default=0, verbose_name="적립금")
    # 주소
    adress = models.CharField(max_length=300, null=True, verbose_name="주소")
    # 가입일
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="가입일")

    class Meta:
        db_table = 't_user' # 테이블 명
        verbose_name = "회원"
        verbose_name_plural = "회원(들)"

    def __str__(self):
        return self.nickname