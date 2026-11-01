from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('library/', views.library, name='library'),
    path('like/<int:song_id>/', views.toggle_like, name='toggle_like'),
]