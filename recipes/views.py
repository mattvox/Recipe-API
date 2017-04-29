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
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
    } for recipe in Recipe.objects.all()]}
    return JsonResponse(data)


def detail(request, recipe_id):
    # fetch that single recipe by its id
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404('Recipe does not exist')

    data = {"url": recipe.url,
            'title': recipe.title,
            'short_description': recipe.short_description,
            'ingredients': recipe.ingredients,
            'instructions': recipe.instructions,
            }
    return JsonResponse(data)
