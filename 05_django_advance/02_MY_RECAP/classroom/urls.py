from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.index, name='index'),

    # 학생 리스트
    path('students/', views.list, name='list'),

    # 개개인 상세 정보 페이지
    path('students/<int:id>/', views.detail, name='detail'),

    # Create 글쓰기 html 필요
    path('students/new', views.new, name='new'),

    # Create한 글 DB 저장
    path('students/create', views.create, name='create'),

    # Update 글 수정 html 필요
    path('students/<int:id>/edit/', views.edit, name='edit'),

    # Update 글 수정 DB 반영
    path('students/<int:id>/update', views.update, name='update'),

    path('students/<int:id>/delete', views.delete, name='delete'),
]