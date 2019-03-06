from django.urls import path
from . import views

app_name = 'kekkatodoke'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('show/', views.show, name='show'),
    path('new/', views.new, name='new'),
    path('detail/<str:subject>/', views.detail, name='detail'),
]