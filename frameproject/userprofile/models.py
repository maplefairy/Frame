from django.contrib.auth.models import User
from django.db import models
from cinema.models import Movie


class Watchlist(models.Model):
    Watchlist_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Watchlist'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.Watchlist_id)


class WatchlistItem(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)

    class Meta:
        db_table = 'WatchlistItem'

    def __str__(self):
        return '{}'.format(self.movie)
