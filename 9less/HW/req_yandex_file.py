import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import re


value_text = input("Введите поисковый запрос: ")
value_lr = input("Введите регион: ")
value_lr = str(value_lr)

headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
payloads = {'text': value_text, 'lr': value_lr}
r = requests.get('https://yandex.ru/search/', params=payloads, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

with open("result.txt", 'a') as file:
    for link in soup.find_all('a', href=re.compile('https:\//')):
        file.write(link.get('href')+'\n')