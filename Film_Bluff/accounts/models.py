# accounts/models.py

from django.db import models

GENRE_CHOICES = [
    ('Action',     'Action'),
    ('Thriller',   'Thriller'),
    ('Drama',      'Drama'),
    ('Comedy',     'Comedy'),
    ('Romance',    'Romance'),
    ('Sci-fi',     'Sci-fi'),
    ('Animation',  'Animation'),
    ('Fantasy',    'Fantasy'),
    ('Mystery',    'Mystery'),
    ('Adventure',  'Adventure'),
    ('Biography',  'Biography'),
]

class Film(models.Model):
    title        = models.CharField(max_length=200)
    genre        = models.CharField(
                      max_length=20,
                      choices=GENRE_CHOICES,
                      default='Drama'
                  )
    actor1       = models.CharField("Actor/Actress 1", max_length=100, blank=True)
    actor2       = models.CharField("Actor/Actress 2", max_length=100, blank=True)
    actor3       = models.CharField("Actor/Actress 3", max_length=100, blank=True)
    actor4       = models.CharField("Actor/Actress 4", max_length=100, blank=True)
    poster_url   = models.URLField("Poster URL", blank=True)
    release_year = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
