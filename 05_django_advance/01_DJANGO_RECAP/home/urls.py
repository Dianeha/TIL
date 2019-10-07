from django.urls import path
from . import views # views.py

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'), # HOST/home/ => views에 index를 실행해라
    path('guess/', views.guess, name='guess'), # HOST/home/guess/
    path('answer/', views.answer, name='answer'), # HOST/home/answer
]