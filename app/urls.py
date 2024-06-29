from django.urls import path, include 
from . import views 

urlpatterns = [
    path('home', views.home, name='home'), 
    path('profile/', views.profile, name='profile'),
    path('edit_profil/', views.edit_profil, name='edit_profil'),
    path('signup/', views.signup, name='signup'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('search:', views.search, name='search'),
]