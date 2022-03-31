from unicodedata import name
from django.urls import path
from . import views

app_name = "Order"

urlpatterns = [
    path('order/', views.order, name="order"),
    path('order/order_des/',views.order_des, name="order_des"),
    path('order/order_des/custom1/',views.custom1 , name="custom1"),
    path('order/order_des/custom1/custom2/',views.custom2 , name="custom2"),
    path('order/order_des/custom1/custom2/customend', views.customend, name="customend"),
    path('payment/', views.payment,name="payment"),
]
