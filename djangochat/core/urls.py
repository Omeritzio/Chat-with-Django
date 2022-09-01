from unicodedata import name
from django.urls import path, include
from django.contrib.auth import views as auth_views

from. import views 


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/',views.signup, name='sign up'),
    path('login/' ,auth_views.LoginView.as_view(template_name='core/logout.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout')
    
]
