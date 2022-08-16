from django.urls import path
from mainapp import views

urlpatterns = [
    path('list/', views.movie_list, name='Movie_list_link'),
    path('list/<int:movie_id>', views.movie_details, name='Movie_details_link')
]
