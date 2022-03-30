from django.urls import path
from user import views

app_name = "Login"

urlpatterns = [
    path('login/', views.login, name='user_login'), # 로그인 창

    path('register/', views.register, name="user_register"), # 회원가입 창

    path('find/', views.find_pw, name="find_pw"), # Pw 찾는페이지

    path('list/', views.magazine_list, name="magazine_list"), # 매거진 리스트
    
    # path('detail/<int:pk>', views.magazine_detail, name="magazine_detail"), # 매거진 상세 
    path('detail/', views.magazine_detail, name="magazine_detail"), # ui설게용 매거진 상세

]
