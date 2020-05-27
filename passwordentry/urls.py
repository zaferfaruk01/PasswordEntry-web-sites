
from django.urls import path
from . import views

 #<int ile movies/2 yazdığı zaman ordaki 2 yi alcıaz


urlpatterns = [

    path('', views.index, name='passwordentry'),
    path('islem/', views.islem, name='islem'),
    
    #path('<int:movie_id>', views.detail, name='detail'),
    
]
