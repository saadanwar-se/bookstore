from django.urls import path
from .views import RegisterAPI, LogoutAPI
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('token/', obtain_auth_token, name='token_obtain'),
    path('logout/', LogoutAPI.as_view(), name='logout'),

]
