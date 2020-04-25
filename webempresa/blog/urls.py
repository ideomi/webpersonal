from django.urls import path
from .  import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/', views.blog_category, name='blog_category'),
]
