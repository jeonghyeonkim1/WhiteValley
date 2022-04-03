from django.urls import path
from . import views

app_name = "Main"

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('admin/', views.admin, name="admin"),
    path('admin/member/', views.admin_member, name="admin_member"),
    path('admin/point/', views.admin_point, name="admin_point"),
    path('admin/account/', views.admin_account, name="admin_account"),
    path('admin/account/add/', views.account_add, name="account_add"),
    path('admin/account/delete/<str:bank>/', views.account_delete, name="account_delete"),
]
