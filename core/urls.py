from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('user/<str:pk>', views.user_info, name="user-info"),
    path('info', views.info, name="info"),
]
