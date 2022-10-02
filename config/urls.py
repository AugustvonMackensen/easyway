"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_login, name = 'index_login' ),
    path('index', views.index, name= 'index'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),

    #qna
    path('notice/', include('notice.urls')),
    #공지
    path('main/', include('main.urls')),

    #네이버 크롤링
    path('naver_crawling/', include('naver_crawling.urls')),

    #covid
    path('covid/', include('covid.urls')),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('users/password_reset_complete/', views.view_complete, name="password_reset_complete"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete2'),
    path('account/', include('allauth.urls')),  #소셜로그인 추가부분
    path('account/google/login/callback/index/',views.index),
    path('account/kakao/login/callback/index/',views.index),
    path('account/naver/login/callback/index/',views.index),
]
