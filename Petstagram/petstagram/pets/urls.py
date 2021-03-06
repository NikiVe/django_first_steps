from django.urls import path

from petstagram.pets.views import DeletePetView, UpdatePetView, CreatePetView, PetListView, \
    PetDetailsView, LikePetView, CommentPetView

urlpatterns = [
    path('', PetListView.as_view(), name='list pets'),
    path('detail/<int:pk>/', PetDetailsView.as_view(), name='pet details'),
    path('comment/<int:pk>/', CommentPetView.as_view(), name='comment pet'),
    path('like/<int:pk>/', LikePetView, name='like pet'),
    path('edit/<int:pk>/', UpdatePetView.as_view(), name='edit pet'),
    path('delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),
    path('create/', CreatePetView.as_view(), name='create pet'),
]