from django.urls import path
from . import views 
urlpatterns = [   
    path('', views.index, name='home'),
    path('shops', views.shops, name='skin'), #название страницы при переходе 
]