from django.shortcuts import render
from . models import Movie
from django.http import Http404
from django.views.generic import DetailView
from bs4 import BeautifulSoup

def movie(request, movie_id):
    #movie =Movie.objects.get(pk=movie_id)
    movie = Movie.objects.all()
    if movie is not None:
        return render(request,'movies/movie.html', {'movie':movie})
    else:
        raise Http404('NOT EXIST')

