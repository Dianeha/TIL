from django.urls import path
from . import views  # 같은 위치안에 있는 views.py 파일 불러온 것.

urlpatterns = [
    # Create
    path('articles/new/', views.new),
    path('articles/create/', views.create),  # /board/articles/create

    # Read
    path('articles/', views.index),  # DOMAIN/board/articles/
    path('articles/<int:article_id>/', views.show),  # /board/articles/1
    # Update
    # Delete
    path('articles/<int:article_id>/delete/', views.delete),  # /board/articles/1/delete
]
