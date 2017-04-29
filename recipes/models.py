from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import URLValidator


class Recipe(models.Model):
    """
    Recipe model
    """
    url = models.CharField(validators=[URLValidator], max_length=500)
    title = models.CharField(max_length=100)
    description = models.TextField()
    cook_time = ArrayField(models.CharField(max_length=200), default=list)
    difficulty = models.CharField(max_length=40)
    servings = models.CharField(max_length=40)
    tags = ArrayField(models.CharField(max_length=40), default=list)
    ingredients = ArrayField(models.CharField(max_length=200), default=list)
    instructions = ArrayField(models.TextField(), default=list)
