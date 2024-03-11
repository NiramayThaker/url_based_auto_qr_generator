from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('user/<str:pk>', views.user_info, name="user-info"),
    path('info', views.info, name="info"),
    path('sign-up', views.sign_up, name="sign-up"),
    path("", include("django.contrib.auth.urls")),
]
