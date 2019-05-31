from django.urls import (
    reverse,
    path,
    include
)

from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),   
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup')
]