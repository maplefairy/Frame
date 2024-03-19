from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Movie, Category, Review
from .forms import MovieForm
from django.contrib.auth.models import User


# Create your views here.
def allmoviescat(request, c_slug=None):
    c_page = None
    movies_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        movies_list = Movie.objects.all().filter(category=c_page)
    else:
        movies_list = Movie.objects.all()

    paginator = Paginator(movies_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        movies = paginator.page(page)
    except (EmptyPage, InvalidPage):
        movies = paginator.page(paginator.num_pages)
    return render(request, "category.html", {'category': c_page, 'movies': movies,
                                             'movies_list': movies_list})


def moviedetail(request, c_slug, movie_slug):
    movie = get_object_or_404(Movie, category__slug=c_slug, slug=movie_slug)
    try:
        movie = Movie.objects.get(category__slug=c_slug, slug=movie_slug)
    except Exception as e:
        raise e
    return render(request, "movie.html", {'movie': movie})


def add_movie(request):
    categories = Category.objects.all()
    f = MovieForm(request.POST or None, request.FILES or None)
    if f.is_valid():
        movie = f.save(commit=False)
        movie.user = request.user
        movie.save()
        return redirect('userprofile:profile')
    return render(request, 'add_movie.html', {'categories': categories, 'f': f})


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        image = request.FILES['image']

        category = Category(
            name=name,
            description=description,
            image=image,
            slug=slug
        )
        category.save()
        return redirect('/')

    return render(request, 'add_category.html')


@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('userprofile:profile')
    return render(request, 'delete_movie.html', {'movie': movie})


@login_required
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.user != movie.user:
        return redirect('cinema:profile')

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('userprofile:profile')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'update_movie.html', {'form': form})


def review_page(request, id):
    movie_details = get_object_or_404(Movie, id=id)
    user = request.user
    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        movie_review = request.POST.get('review_title')
        review_text = request.POST.get('review_text')

        if not movie_review:
            # Handle the case where the review title is empty
            # You can return an error message or redirect the user to the review page
            pass

        movie_reviews = Review(user=user, movie=movie_details, rating=star_rating, review_title=movie_review)
        movie_reviews.save()

        rating_details = Review.objects.filter(movie=movie_details)
        context = {'reviews': rating_details}
        return redirect('cinema:moviescatdetail', c_slug=movie_details.category.slug, movie_slug=movie_details.slug)

    rating_details = Review.objects.filter(movie=movie_details)
    context = {'reviews': rating_details}
    return render(request, "review_page.html", context)
