from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register_user, name='register_user'),
    path('api/login/', views.login_user, name='register_user'),
    path('api/get_user/', views.user_by_email_login, name='users_list'),
    path('api/update_user/', views.update_user, name='users_list'),
]