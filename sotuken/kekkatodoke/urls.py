from django.urls import path
from . import views

app_name = 'kekkatodoke'
urlpatterns = [
    path('', views.top, name='top'),
    path('new/', views.new, name='new'),
    path('about/', views.about, name='about'),
    path('detail/', views.detail, name='detail'),
    path('show/', views.show, name='show'),
]