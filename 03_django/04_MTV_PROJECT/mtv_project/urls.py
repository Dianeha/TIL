from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),  # board app 에 urls 파일로 밀어서 보내겠다.
]
