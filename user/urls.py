from django.urls import path
from . import views

 #<int ile movies/2 yazdığı zaman ordaki 2 yi alcıaz


urlpatterns = [

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

]

