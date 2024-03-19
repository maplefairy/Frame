from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from userprofile.models import Watchlist, WatchlistItem
from cinema.models import Movie
from django.shortcuts import render


def _watchlist_id(request):
    watchlist = request.session.session_key
    if not watchlist:
        watchlist = request.session.create()
    return watchlist


def add_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    try:
        watchlist = Watchlist.objects.get(Watchlist_id=_watchlist_id(request))
    except Watchlist.DoesNotExist:
        watchlist = Watchlist.objects.create(Watchlist_id=_watchlist_id(request))
        watchlist.save()
    try:
        WatchlistItem.objects.get(movie=movie, watchlist=watchlist)
        messages.info(request, 'This movie is already in your watchlist.')
    except WatchlistItem.DoesNotExist:
        WatchlistItem.objects.create(movie=movie, watchlist=watchlist)
    return redirect('userprofile:watchlist_detail')


def watchlist_detail(request, watchlist_items=None):
    watchlist = get_object_or_404(Watchlist, Watchlist_id=_watchlist_id(request))
    watchlist_items = WatchlistItem.objects.filter(watchlist=watchlist)
    return render(request, 'profile.html', {'watchlist_items': watchlist_items})


def full_remove(request, movie_id):
    watchlist = Watchlist.objects.get(Watchlist_id=_watchlist_id(request))
    movie = get_object_or_404(Movie, id=movie_id)
    watchlist_item = WatchlistItem.objects.get(movie=movie, watchlist=watchlist)
    watchlist_item.delete()
    return redirect('userprofile:watchlist_detail')


@login_required
def profile(request):
    user_add_movies = Movie.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user_add_movies': user_add_movies})

