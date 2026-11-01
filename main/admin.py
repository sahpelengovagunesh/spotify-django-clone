from django.contrib import admin
from .models import Album, Song, LikedSong

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(LikedSong)
