from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import *
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('',home,name='home'),
    path('post/<int:post_id>/',post_detail,name='post_detail'),
    path('create/',create_post, name='create_post'),
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'), 
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
 

]
