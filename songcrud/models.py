from django.db import models


class Artiste(models.Model):
    first_name = models.CharField()
    last_name = models.CharField
    age = models.IntegerField()


class Song(models.Model):
    title = models.TextField()
    date = models.DateField()
    released = models.BooleanField()
    likes = models.ManyToManyField('self', null=True)
    artiste_id = models.ForeignKey(Artiste)


class Lyrics(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song)
