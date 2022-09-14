from django.urls import path
from user.views import (
    AccountView,
    UpdatePassowrd,
    CreateAccountView
)

app_name = 'user'

urlpatterns = [
    path('me', AccountView.as_view(), name='me'),
    path('change-password', UpdatePassowrd.as_view(), name='change-password'),
    path('register', CreateAccountView.as_view(), name='register-password')
]