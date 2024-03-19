from django.shortcuts import render
from cinema.models import Movie, Category
from django.db.models import Q


# Create your views here.


def searchresult(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.all().filter(Q(name__contains=query) | Q(description__contains=query) | Q(actors__contains=query))
    return render(request, 'search.html', {'query': query, 'movies': movies})
