from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flight_tap/', views.flight_tap, name='flight_tap'),
    path('place_share/', views.place_share, name= 'place_share'),
    path('drone_trading/', views.drone_trading, name= 'drone_trading'),
    path('kakaotalk_chat/', views.kakaotalk_chat, name='kakaotalk_chat'),
]