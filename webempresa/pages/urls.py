from django.urls import path
from .  import views

urlpatterns = [
    #path('', views.blog, name='blog'),
    path('<int:page_id>/<slug:page_slug>', views.pages, name='page'),
]
