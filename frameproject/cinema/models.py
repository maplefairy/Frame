from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('cinema:movies_by_category', args=[self.slug])


class Movie(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cinema', blank=True)
    r_date = models.DateField()
    actors = models.CharField(max_length=250, blank=True)
    trailer = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'cinema'
        verbose_name_plural = 'movies'

    def get_url(self):
        return reverse('cinema:moviescatdetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.review_title)
