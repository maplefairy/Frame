from django.urls import path
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('add/<int:movie_id>/', views.add_watchlist, name='add_watchlist'),
    path('watchlist/', views.watchlist_detail, name='watchlist_detail'),
    path('full_remove/<int:movie_id>/', views.full_remove, name='full_remove'),
 ]
