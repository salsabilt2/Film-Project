from django.db import models

class Film(models.Model):
    title        = models.CharField(max_length=200)
    actor1       = models.CharField("Actor/Actress 1", max_length=100, blank=True)
    actor2       = models.CharField("Actor/Actress 2", max_length=100, blank=True)
    actor3       = models.CharField("Actor/Actress 3", max_length=100, blank=True)
    actor4       = models.CharField("Actor/Actress 4", max_length=100, blank=True)
    poster_url   = models.URLField("Poster URL", blank=True)
    release_year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
