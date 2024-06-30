from django.urls import path, path 
from  account import views 

urlpatterns= [
    path('',views.login, name='login' ),
]
