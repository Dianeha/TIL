from django.urls import path
from . import views

urlpatterns = [
    # utils/cube/<정수>/ # 슬래쉬 = > 앞X뒤o
    path('cube/<int:num>/', views.cube),
    # check_int/<정수>/
    path('check_int/<int:num>/', views.check_int),
    # pick_lotto/
    path('pick_lotto/', views.pick_lotto),
]