
from django.urls import path
from . import views

app_name = "Recommendation"

urlpatterns = [
    path('reviews/',views.reviews, name='reviews'),
    path('product_reviews/',views.reviews, name='product_reviews'),
    path('reviews_detail/',views.reviews_detail, name='reviews_detail'),
    path('tag_reviews/',views.tag_reviews, name='tag_reviews'),
    path('tag_reviews_detail/',views.tag_reviews_detail, name='tag_reviews_detail'),
    path('finished/',views.finished, name='finished'),
    path('finished_detail/',views.finished_detail, name='finished_detail'),
]
