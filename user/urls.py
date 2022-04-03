from django.urls import path
from user import views

app_name = "User"

urlpatterns = [
    # 로그인 및 회원가입 및 PW
    path('login/', views.login, name='user_login'),
    path('logout/',  views.logout, name='user_logout'),
    path('register/', views.register, name="user_register"),
    path('find/', views.find_pw, name="find_pw"), # Pw 찾는페이지
    path('chpw/', views.chpw, name="chpw"), # Pw 변경페이지

    # 매거진
    path('list/', views.magazine_list, name="magazine_list"),
    path('detail/<int:pk>/', views.magazine_detail, name="magazine_detail"), 
    # path('update/<int:pk>/', views.magazine_update, name="magazine_update"),
    path('write/', views.magazine_write, name="magazine_write"),
    path('delete/', views.magazine_delete, name="magazine_delete"),
    # path('per_page/', views.magazine_per_page, name="magazine_per_page"),
    # path('detail/', views.magazine_detail, name="magazine_detail"), # ui설게용 매거진 상세
    path('update/', views.magazine_update, name="magazine_update"), # ui설게용 매거진 상세

    # mypage -------------------------------------------------------------------------------
    path('mypage/', views.mypage, name="mypage"),
]
