from django.urls import path
from . import views

app_name='covid'

urlpatterns = [
    path('region/', views.region, name='region'),
    path('domestic/', views.domestic, name='domestic'),
    path('domtable/', views.domestic_table, name='domtable'),
    path('regtable/', views.regional_table, name='regtable'),
]