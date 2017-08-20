import requests
import django
from bs4 import BeautifulSoup
from .url_scraper import get_urls

HEADERS = {'User-agent': 'Google Chrome'}


def get_recipes(model, headers=HEADERS):
    urls = get_urls()

    for url in urls:
        request = requests.get(url, headers=HEADERS)

        recipe_data = {
            'url': url,
            'title': "",
            'image_url': "",
            'description': "",
            'cook_time': [],
            'difficulty': "",
            'servings': "",
            'tags': [],
            'ingredients': [],
            'methods': [],
        }

        # Parsed HTML
        soup = BeautifulSoup(request.text, "html.parser")

        # Title
        title = soup.find_all("h1", class_="recipe-header__title", limit=1)
        recipe_data['title'] = title[0].get_text()

        # Image URL
        image_parent = soup.find_all("div", class_="img-container")
        image_url = image_parent[0].find_all("img")[0].get("src")
        recipe_data['image_url'] = "https:{}".format(image_url)

        # Description
        description = soup.find_all("div", class_="recipe-header__description", limit=1)
        recipe_data['description'] = description[0].get_text()

        # Cooking/Prep Time/Difficulty/Serving Size
        cook_time = soup.find_all("section", class_="recipe-details__item--cooking-time")

        cook_time_prep = cook_time[0].find_all("span", class_="recipe-details__cooking-time-prep")

        cook_time_cook = cook_time[0].find_all("span", class_="recipe-details__cooking-time-cook")

        if len(cook_time_prep) > 0 and len(cook_time_cook) > 0:
            recipe_data['cook_time'].append(cook_time_prep[0].get_text())
            recipe_data['cook_time'].append(cook_time_cook[0].get_text())
        else:
            recipe_data['cook_time'].append(cook_time[0].get_text())

        difficulty = soup.find_all("section", class_="recipe-details__item--skill-level")
        recipe_data['difficulty'] = difficulty[0].get_text()

        servings = soup.find_all("section", class_="recipe-details__item--servings")
        recipe_data['servings'] = servings[0].get_text()

        # Tags
        tag_parent = soup.find_all("ul", class_="additional-info")
        try:
            tags = tag_parent[0].find_all("li")

            for tag in tags:
                recipe_data['tags'].append(tag.get_text())
        except IndexError:
            pass

        # Ingredients
        ingredients = soup.find_all("li", class_="ingredients-list__item")
        for ingredient in ingredients:
            for part in ingredient.contents:
                    if part.name == "span":
                        part.extract()
            recipe_data['ingredients'].append(ingredient.get_text())

        # Methods/Directions
        methods = soup.find_all("li", class_="method__item")
        for method in methods:
            for part in method.contents:
                if part.name == "span":
                    part.extract()
            recipe_data['methods'].append(method.get_text())

        try:
            recipe = model(url=recipe_data['url'], title=recipe_data['title'], image_url=recipe_data['image_url'], description=recipe_data['description'], cook_time=recipe_data['cook_time'], difficulty=recipe_data['difficulty'], servings=recipe_data['servings'], tags=recipe_data['tags'], ingredients=recipe_data['ingredients'], methods=recipe_data['methods'])
            recipe.save()
            print("{} saved".format(recipe.title))
        except django.db.utils.IntegrityError:
            print('An error occured...')
            pass
