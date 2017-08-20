from .scraper.recipe_scraper import get_recipes
from django.core.management.base import BaseCommand, CommandError
from recipes.models import Recipe


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_recipes(Recipe)
