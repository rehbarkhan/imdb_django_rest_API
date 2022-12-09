from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    website = models.URLField(max_length=255)

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    patform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name='watchlist')
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title