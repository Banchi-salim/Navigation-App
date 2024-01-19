from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    #path('home/', views.homepage, name='home'),
    path('map/', views.index, name='map'),
    #path('login/', views.login_view, name='login'),
    #path('signup/', views.signup_view, name='signup'),
]
