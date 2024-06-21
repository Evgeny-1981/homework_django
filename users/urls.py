from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, email_verification

app_name = UsersConfig.name
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('logout/', LogoutView.as_view(template_name='catalog/home.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
