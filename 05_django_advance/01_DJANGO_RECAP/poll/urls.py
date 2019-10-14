from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('', views.poll_result, name='poll_result'),
    path('/update_poll', views.update_poll, name='update_poll'),
]
