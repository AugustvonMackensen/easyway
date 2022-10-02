from django.urls import path

from . import views


app_name = 'naver_crawling'

urlpatterns = [
    path('', views.naver_crawling, name='naver_crawling'),
    path('naver_title/', views.naver_title, name='naver_title'),
    path('naver_comment/', views.naver_comment, name='naver_comment'),
    #naver_crawling/ = ''
    # path('', views.NaverTitle, name='NaverTitle'),
    # path('', views.NVTitle, name='NVTitle'),
    # path('', views.NVComment, name='NVComment'),
]