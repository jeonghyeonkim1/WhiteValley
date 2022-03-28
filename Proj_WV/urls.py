from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('whitevalley/', include('shop.urls')),
    path('whitevalley/', include('user.urls')),
    path('whitevalley/', include('order.urls')),
    path('whitevalley/', include('recommendation.urls')),
    path('whitevalley/', include('cs.urls')),
]
