from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    # Admin 
    path('admin/', admin.site.urls),
    # Frontend 
    path('', views.frontend, name="frontend"),
    # Backend 
    path('backend/', views.backend, name="backend"),
    path('login/', views.Login, name="login"),
    path('login_user', views.LoginUser, name="login_user"),
    path('logout/', views.LogoutUser, name="logout"),
]