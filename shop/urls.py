from django.urls import path
from . import views

app_name = "Main"

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('admin/', views.admin, name="admin"),
    path('admin/member/', views.admin_member, name="admin_member"),
]
