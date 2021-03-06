from django.urls import path, include

from accounts.views import signup_user, user_profile, signout_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>', user_profile, name='user profile'),
    path('profile/', user_profile, name='current user profile'),
    path('signup/', signup_user, name='signup user'),
    path('signout/', signout_user, name='signout user'),
]
