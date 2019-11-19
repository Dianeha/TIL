from django.urls import path
from . import views

app_name = 'todos' # 필요없긴함

urlpatterns = [
    path('', views.create_todo)
]