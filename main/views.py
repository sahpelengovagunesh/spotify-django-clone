from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song, LikedSong
from django.contrib.auth.decorators import login_required

def home(request):
    albums = Album.objects.all()
    return render(request, 'main/index.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = album.songs.all()
    return render(request, 'main/album_detail.html', {'album': album, 'songs': songs})

@login_required
def library(request):
    liked_songs = LikedSong.objects.filter(user=request.user)
    return render(request, 'main/library.html', {'liked_songs': liked_songs})

@login_required
def toggle_like(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    liked, created = LikedSong.objects.get_or_create(user=request.user, song=song)
    if not created:
        liked.delete() # Artıq bəyənilibsə, saxlanılanlardan çıxar
    return redirect(request.META.get('HTTP_REFERER', 'home'))