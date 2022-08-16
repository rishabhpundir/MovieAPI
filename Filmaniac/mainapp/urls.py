from django.urls import path
from mainapp import views

urlpatterns = [
    path('list/', views.MovieListAPIView.as_view(), name='Movie_list_link'),
    path('list/<int:movie_id>', views.MovieDetailsAPIVIew.as_view(), name='Movie_details_link')
]
