from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.


class MovieResources(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        reseource_name = 'movies'
        excludes = ['date_created']
