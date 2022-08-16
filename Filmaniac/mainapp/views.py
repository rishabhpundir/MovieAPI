from django.shortcuts import render
from mainapp.models import Movie
from django.http import JsonResponse
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# Function View

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method== 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method== 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method== 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method== 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method== 'DELETE':
        movie.delete()
        return Response('Item deleted!', status=status.HTTP_204_NO_CONTENT)
