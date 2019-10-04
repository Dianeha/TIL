from django.urls import path
from . import views # views.py

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'), # HOST/home/
    path('guess/', views.guess, name='guess'), # HOST/home/hi/
    path('answer/', views.answer, name='answer'),
]