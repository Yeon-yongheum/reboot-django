from django.urls import path
from . import views

app_name = 'pastlifes'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('result/', views.result, name='result'),
    # path('<int:pastlife_pk>/', views.detail),
]