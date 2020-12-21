from django.urls import path, include
from .receivers import *
from petstagram.accounts.views import user_profile, SignUpView, SignOutView, SignInView, UserProfileView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', user_profile, name='user profile'),
    path('profile/', UserProfileView.as_view(), name='current user profile'),
    path('signin/', SignInView.as_view(), name='signin user'),
    path('signup/', SignUpView.as_view(), name='signup user'),
    path('signout/', SignOutView.as_view(), name='signout user'),
]
