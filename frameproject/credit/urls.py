from django.urls import path
from . import views
app_name = 'credit'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('delete_account', views.delete_account, name='delete_account'),
]
