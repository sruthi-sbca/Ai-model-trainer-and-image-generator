from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('train/', views.index, name='trainingpage'),
    path('run_bat_stream/', views.run_bat_stream, name='run_bat_stream'),
    path('get_progress/', views.get_progress, name='get_progress'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
