# Taskmanager6

# Taskmanager 6

1) cd taskmanager6

2) django-admin startproject taskmanager6

3) cd taskmanager6

4) python3 [manage.py](http://manage.py) startapp djangouploads

5) Setting file modificam: 

INSTALLED APPS:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangouploads',
]
```

TEMPLATES: 

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

si la URLs:

```python
STATIC_URL = 'media/'
MEDIA_ROOT = ''
MEDIA_URL = ''
```

6) in URLS din proiect punem urmatorul cod:

```python
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangouploads.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
```

7) facem un file [urls.py](http://urls.py) → in app si inseram urmatorul cod:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/<int:movie_id>', views.movie),
]

urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
```

8) In admin adaugam next code:

```python
from django.contrib import admin
from . models import Movie

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Movie, MovieAdmin)
```

9) in views punem: 

```
from django.shortcuts import render
from . models import Movie
from django.http import Http404
from django.views.generic import DetailView
from bs4 import BeautifulSoup

def movie(request, movie_id):
    movie =Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request,'movies/movie.html', {'movie':movie})
    else:
        raise Http404('NOT EXIST')

with open('djangouploads/templates/movies/movie4.html') as file:
    src = file.read()
soup = BeautifulSoup(src,'lxml')
gettext = soup.body.a.text

```

10) In app facem urmatoarele foldere: files → din files: covers

11) Tot in app facem un folder templates dupa in templates → movies si aducem fileul movie.html in movies

12) in covers adaugam imagini

13) In models.py adaugam:

from django.db import models

class Movie(models.Model):
    name =models.CharField(max_length=200)
    image= models.ImageField(upload_to='djangouploads/files/covers')

