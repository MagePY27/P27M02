from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.asset_list, name='asset_list'),
    re_path('asset/(?P<asset_id>[0-9]+)/update/', views.asset_update),
    re_path('asset/(?P<asset_id>[0-9]+)/delete/', views.asset_delete),
    path('asset/add/', views.asset_add),
]
