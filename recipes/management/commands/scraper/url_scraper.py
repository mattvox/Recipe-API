import re
import requests
from bs4 import BeautifulSoup

HEADERS = {'User-agent': 'Google Chrome'}
URL = "https://www.bbcgoodfood.com/sitemap.xml"
RECIPE_URL_BASE = "https://www.bbcgoodfood.com/recipes"


def get_urls(url=URL):
    request = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(request.text, "html.parser")
    # check whether the status code is OK (200)
    data = []

    # for link in soup.find_all("loc"):
    #     recipe = link.text
    #     recipe_test = re.compile("http://www.bbcgoodfood.com/recipe")
    #     if recipe_test.match(recipe):
    #         data.append(recipe)

    for index, link in enumerate(soup.find_all("loc")):
        recipe = link.text
        recipe_test = re.compile(RECIPE_URL_BASE)
        if recipe_test.match(recipe):
            data.append(recipe)

        if index >= 2000:
            break

        print(data)
    return data
