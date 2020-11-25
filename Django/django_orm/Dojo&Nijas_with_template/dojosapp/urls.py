from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
     path('adddojo', views.adddojo),
       path('addNinja', views.addNinja),
]
