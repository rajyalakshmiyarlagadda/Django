from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from usersApp import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='usersApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersApp/logout.html'), name='logout'),
    path('signup/', user_views.signUp, name='signup')
]