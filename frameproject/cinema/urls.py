from django.urls import path
from . import views
app_name = 'cinema'
urlpatterns = [
    path('', views.allmoviescat, name='allmoviescat'),
    path('review_page/<int:id>/', views.review_page, name='review_page'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('update_movie/<int:movie_id>/', views.update_movie, name='update_movie'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('<slug:c_slug>/', views.allmoviescat, name='movies_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/', views.moviedetail, name='moviescatdetail'),


]
