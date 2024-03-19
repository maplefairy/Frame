from django.contrib import admin
from .models import Category, Movie, Review


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'actors', 'trailer', 'r_date']
    list_editable = ['trailer']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review_title', 'rating']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
