from django.views.decorators.cache import cache_page
from django.urls import path
from .views import (
    AccountView,
    UpdatePassowrd,
    CreateAccountView
)

app_name = 'users'

urlpatterns = [
    path('me', cache_page(60 * 1)(AccountView.as_view()), name='me'),
    path('change-password', UpdatePassowrd.as_view(), name='change-password'),
    path('register', CreateAccountView.as_view(), name='register-password')

]
