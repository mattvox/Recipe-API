# import json

# from django.shortcuts import render
from django.http import Http404, JsonResponse

from .models import Recipe


def recipes(request):
    # TODO -> how the hell do I do pagination?
    data = {"data": [{
        'id': recipe.id,
        'url': recipe.url,
        'title': recipe.title,
        'image_url': recipe.image_url,
        'description': recipe.description,
        'cook_time': recipe.cook_time,
        'difficulty': recipe.difficulty,
        'servings': recipe.servings,
        'tags': recipe.tags,
        'ingredients': recipe.ingredients,
        'methods': recipe.methods,
    } for recipe in Recipe.objects.all()]}
    return JsonResponse(data)


def detail(request, recipe_id):
    # fetch that single recipe by its id
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404('Recipe does not exist')

    data = {'id': recipe.id,
            "url": recipe.url,
            'title': recipe.title,
            'image_url': recipe.image_url,
            'description': recipe.description,
            'cook_time': recipe.cook_time,
            'difficulty': recipe.difficulty,
            'servings': recipe.servings,
            'tags': recipe.tags,
            'ingredients': recipe.ingredients,
            'methods': recipe.methods,
            }
    return JsonResponse(data)
