from django.urls import path
from django.urls import path
from .views import RegisterAPI,RegisterView,LoginView
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns=[
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('regi/',RegisterView.as_view(),name='regi'),
    path('log/',LoginView.as_view(),name='log'),

]