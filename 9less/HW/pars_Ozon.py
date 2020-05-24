import re
import requests
import os
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

URL = 'https://www.ozon.ru/category/trenazhery-ganteli-shtangi-32523/'
name_folder = 'oz_sport'
os.mkdir(name_folder)

headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
page = requests.get(URL, headers=headers)
page.raise_for_status()

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('img', src=re.compile('https:\//\w+\.\w+\.\w+\/\w+\/\w+|-|(\w+\/\w+\/\d+\.jpg)|(\/\d+\.jpg)'))
print(results)

print(type(results))
print(len(results))


def save_img(img, file_name):
    with open(file_name, "wb") as handler:
        handler.write(img.content)


count = 0

for result in results:
    link = result['src']
    img_data = requests.get(link)
    file_name = name_folder + "/" + str(count) + ".jpg"
    save_img(img_data, file_name)
    count += 1
