from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='HOME'),
    path('index/', views.index, name='index'),
]
