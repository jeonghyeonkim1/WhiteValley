from django.urls import path
from cs import views

app_name = "Cs"

urlpatterns = [
    path("write/", views.notice_write, name="notice_write"),
    path("detail/<int:pk>/", views.notice_detail, name="notice_detail"),
    path("list/", views.notice_list, name="notice_list"),
    path('update/<int:pk>/', views.notice_update, name="notice_update"),
    path('delete/', views.notice_delete, name="notice_delete"),
    path("event/write/", views.event_write, name="event_write"),
    path("event/detail/<int:pk>/", views.event_detail, name="event_detail"),
    path("event/list/", views.event_list, name="event_list"),
    path('event/update/<int:pk>/', views.event_update, name="event_update"),
    path('event/delete/', views.event_delete, name="event_delete"),
]
