from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # chat app general
    path('', views.home_main, name='home_main'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    
    # room
    path('rooms/', views.home, name='home'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('create_room/', views.create_room, name='create_room'),
    path('delete_room/', views.delete_room, name='delete_room'),
    path('edit_room/<int:id>/', views.edit_room, name='edit_room'),

    # villa
    path('villa/<str:villa_name>/', views.villa, name='villa'),
    path('villa/<str:villa_name>/room/<str:room_name>/', views.villa_room, name='villa_room'),
]