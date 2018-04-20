from django.urls import path

from api import views


urlpatterns = [
    path('posts/', views.post_list),
    path('posts/<int:post_id>/', views.post_detail),
]