from django.db import models

from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    cover_image = models.URLField(max_length=500, blank=True, null=True) # İnternet linki üçün
    
    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=10) # məsələn: "3:45"
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)

    def __str__(self):
        return self.title

class LikedSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')
