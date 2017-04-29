import requests
from bs4 import BeautifulSoup

headers = {'User-agent': 'Google Chrome'}

url = "https://www.bbcgoodfood.com/recipes/2869/new-york-cheesecake"
url = "https://www.bbcgoodfood.com/recipes/1805655/haricot-bean-and-truffle-mash"
url = 'https://www.bbcgoodfood.com/recipes/1167651/chicken-and-chorizo-jambalaya'
url = "https://www.bbcgoodfood.com/recipes/9022/baked-stuffed-romano-peppers"

request = requests.get(url, headers=headers)

print(request.status_code)

recipe_data = {
    'title': "",
    'description': "",
    'snapshot': {
        'cook_time': [],
        'difficulty': "",
        'serves': "",
    },
    'tags': [],
    'ingredients': [],
    'methods': [],
}

# Parsed HTML
soup = BeautifulSoup(request.text, "html.parser")

# Title
title = soup.find_all("h1", class_="recipe-header__title", limit=1)
recipe_data['title'] = title[0].get_text()

# Description
description = soup.find_all("div", class_="recipe-header__description", limit=1)
recipe_data['description'] = description[0].get_text()

# Cooking/Prep Time/Difficulty/Serving Size
cook_time = soup.find_all("section", class_="recipe-details__item--cooking-time")

cook_time_prep = cook_time[0].find_all("span", class_="recipe-details__cooking-time-prep")

cook_time_cook = cook_time[0].find_all("span", class_="recipe-details__cooking-time-cook")

if len(cook_time_prep) > 0 and len(cook_time_cook) > 0:
    recipe_data['snapshot']['cook_time'].append(cook_time_prep[0].get_text())
    recipe_data['snapshot']['cook_time'].append(cook_time_cook[0].get_text())
else:
    recipe_data['snapshot']['cook_time'].append(cook_time[0].get_text())

difficulty = soup.find_all("section", class_="recipe-details__item--skill-level")
recipe_data['snapshot']['difficulty'] = difficulty[0].get_text()

serves = soup.find_all("section", class_="recipe-details__item--servings")
recipe_data['snapshot']['serves'] = serves[0].get_text()

# Tags
tag_parent = soup.find_all("ul", class_="additional-info")
tags = tag_parent[0].find_all("li")
for tag in tags:
    recipe_data['tags'].append(tag.get_text())


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

# Print Statements for Testing
print(recipe_data)


# import pdb; pdb.set_trace()
