from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_page, name='register_page'),
    path('api/register/', views.register_user, name='register_user'),
    path('api/users/', views.users_list, name='users_list'),
]