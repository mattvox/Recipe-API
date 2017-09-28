from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import URLValidator


class Recipe(models.Model):
    """
    Recipe model
    """

    def __str__(self):
        return self.title

    url = models.CharField(validators=[URLValidator], max_length=500, unique=True)
    title = models.CharField(max_length=100)
    image_url = models.CharField(validators=[URLValidator], max_length=1000)
    description = models.TextField()
    cook_time = ArrayField(models.CharField(max_length=200), default=list)
    difficulty = models.CharField(max_length=100)
    servings = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=100), default=list)
    ingredients = ArrayField(models.CharField(max_length=500), default=list)
    methods = ArrayField(models.TextField(), default=list)
