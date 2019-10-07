from django.urls import path
from . import views # views.py

app_name = 'board'


urlpatterns = [ # 여기가 없으면 무조건 에러난다
    # HOST/board/ 이렇게 url이 들어오면 => views에 board 함수와 묶였으니 board를 실행해라는 뜻
    path('', views.index, name='index'), # 얘의 이름은 이제 board:index
]