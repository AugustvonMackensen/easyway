from django.urls import path
# 장고가 제공하는 로그인뷰와 로그인/로그아웃 기능 사용할 것임
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'users'

urlpatterns = [
    path('', views.index_login, name='index_login'),
    path('login/index/', views.index, name='index'),
    # path('user/create/', views.user_vreate, name='user_create'),
    # path('login/',views.login, name='login'),
    # path('logout/',views.logout, name='logout'),
    # path('user/info/', views.user_info, name='user_info'),
    # path('user/info/update', views.user_info_update, name='user_info_update'),
    # path('user/info/delete', views.user_delete, name='user_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('send_email/', views.send_email, name='send_email'),

    #회원정보 업데이트
    path('update/', views.update, name='update'),
    #회원삭제
    path('delete/', views.delete, name='delete'),
    #비밀번호 변경
    path('password/', views.change_password, name='password'),

    #아이디 찾기
    path('forgot_id/', views.forgot_id, name='forgot_id'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)