from django.urls import path
from . import views, admin
from django.contrib.auth import views as auth_views
#from .views import ProfileUpdateView, ProfileDetailView, UserRegisterView, UserLoginView, UserLogoutView
from .views import UserLoginView, UserRegisterView
from .views import index

urlpatterns = [

    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('monitoring', views.monitoring, name='monitoring'),
    path('test', views.test, name='test'),
    path('help', views.help, name='help'),
    path('authorization', views.authorization, name='authorization'),
    #path('register/', views.register, name='register'),
    #path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
]

