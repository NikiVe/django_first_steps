from django.urls import path

from app_01.views import index

urlpatterns = [
    path('', index)
]
