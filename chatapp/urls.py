from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('direct/<username>/', views.directs, name='directs'),
]