from django.urls import path
from . import views

app_name = 'sns'

urlpatterns = [
    path('newsfeed/', views.posting_list, name='posting_list'),
    path('postings/<int:posting_id>/', views.posting_detail, name='posting_detail')
]
