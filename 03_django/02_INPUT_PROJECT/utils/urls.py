from django.urls import path
from . import views

urlpatterns = [
    # 'utils/'
    path('', views.index),  # utils/
    path('art/', views.art),  # utils/art/
    path('output/', views.output),  # utils/art/
    path('throw/', views.throw),
    path('catch/', views.catch),
]