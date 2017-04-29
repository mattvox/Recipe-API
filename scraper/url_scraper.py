import re
import requests
from bs4 import BeautifulSoup

headers = {'User-agent': 'Google Chrome'}
url = "https://www.bbcgoodfood.com/sitemap.xml"
request = requests.get(url, headers=headers)
soup = BeautifulSoup(request.text, "html.parser")

print(request.status_code)

i = 0
for link in soup.find_all("loc"):
    if i < 20:
        recipe = link.text
        recipe1 = re.search(r'\bhttps://www.bbcgoodfood.com/recipe\b', recipe)
        # if link.find_all(text=re.compile('')):
        # if recipe1:
        recipe_test = re.compile("http://www.bbcgoodfood.com/recipe")

        if recipe_test.match(recipe):
            print(recipe)
        # print(recipe1)
        # else:
        #     print('nope')
        # print(recipe)
        i += 1


# for link in soup.findAll("li", class_="ingredients-list__item"):
#     print(link.prettify())
