from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('post-comment/', views.post_comment, name='post_comment'),
    path('check-auth/', views.check_auth, name='check_auth'),
]