from django.urls import path
from . import views

app_name = 'kekkatodoke'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('look/', views.look, name='look'),
    path('send/', views.send, name='send'),
    path('detail/<str:subject>/', views.detail, name='detail'),
]