from django.urls import path
from . import views # views.py

app_name = 'board'


urlpatterns = [ # 여기가 없으면 무조건 에러난다
    # HOST/board/ 이렇게 url이 들어오면 => views에 board 함수와 묶였으니 board를 실행해라는 뜻
    path('', views.index, name='index'), # 얘의 이름은 이제 board:index
    
    # Read 글 목록(list) render로 html 파일 내보내야함
    path('articles/', views.list, name='list'),
    # Read 글 상세(detail) render html
    path('articles/<int:id>/', views.detail, name='detail'),

    # Create 글 쓰기(new) render html
    path('articles/new/', views.new, name='new'),
    # Create 글 DB저장(create)    
    path('articles/create/', views.create, name='create'),

    # Update 글 수정쓰기(edit) render html
    path('articles/<int:id>/edit/', views.edit, name='edit'),
    # Update글 실제DB수정(update)
    path('articles/<int:id>/update/', views.update, name='update'),

    # Delete 글 삭제(delete)
    path('articles/<int:id>/delete/', views.delete, name='delete'),
]