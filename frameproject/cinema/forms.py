from .models import Movie, Category
from django import forms


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'r_date', 'category', 'trailer', 'image', 'slug', 'user', 'actors']
