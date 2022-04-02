from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

app_name = "User"

urlpatterns = [
    path('login/', views.login, name='user_login'), # 로그인 창

    path('logout/',  views.logout, name='user_logout'),

    path('register/', views.register, name="user_register"), # 회원가입 창

    path('find/', views.find_pw, name="find_pw"), # Pw 찾는페이지

    path('chpw/<int:pk>', views.chpw, name="chpw"), # Pw 변경페이지

    path('magazine/list/', views.magazine_list, name="magazine_list"), # 매거진 리스트
    
    # path('detail/<int:pk>', views.magazine_detail, name="magazine_detail"), # 매거진 상세 
    path('detail/', views.magazine_detail, name="magazine_detail"), # ui설게용 매거진 상세
    
    # path('update/<int:pk>', views.magazine_update, name="magazine_update"), # 매거진 수정
    path('update/', views.magazine_update, name="magazine_update"), # ui설게용 매거진 상세

    path('write/', views.magazine_write, name="magazine_write"), # 매거진 작성

    path('delete/', views.magazine_delete, name="magazine_delete"), # 매거진 삭제

    # 장고에서 지원하는 비밀번호 찾기
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # mypage -------------------------------------------------------------------------------
    path('mypage/', views.mypage, name="mypage"),
]
