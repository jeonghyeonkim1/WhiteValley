from django.db import models

# Create your models here.

# class User(models.Model):
#     # 관리자 여부
#     admin = models.BooleanField(verbose_name="관리자모드", null=False)
#     # 이메일
#     email = models.EmailField(max_length=60, verbose_name="이메일", null=False, unique=True)
#     # 비밀번호
#     password = models.CharField(max_length=100, verbose_name="비밀번호", null=False)
#     # 닉네임
#     nickname = models.CharField(max_length=50, verbose_name="닉네임", null=False, unique=True)
#     # 연락처
#     contact = models.IntegerField(verbose_name="연락처", null=False)
#     # 적립금
#     point = models.IntegerField(verbose_name="적립금", null=False, default=0)
#     # 주소
#     destination = models.CharField(max_length=200, verbose_name="주소")
#     # 누적결제금액
#     acm_amount = models.IntegerField(verbose_name="누적결제금액", null=False)
#     # 가입일
#     reg_date = models.DateTimeField(auto_now_add=True, verbose_name="가입일", null=False)

#     class Meta:
#         db_table = 'User' # 테이블 명
#         verbose_name = "회원정보"
#         verbose_name_plural = "회원(들)"

    # class __str__(self):
    #     return self.nickname