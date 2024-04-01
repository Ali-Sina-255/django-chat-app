from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('directs/<username>/', views.directs, name='directs'),
]