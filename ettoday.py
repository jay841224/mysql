import requests
from bs4 import BeautifulSoup

def has_title(tag):
    return tag.has_attr('title')

hml = 'https://www.ettoday.net/'

r = requests.get(hml)

soup = BeautifulSoup(r.text, 'html.parser')
f1 = soup.find('div', 'block block_1 infinite_scroll')
f2 = soup.find('div', 'block_content')
f3 = soup.find('div', 'part_list_7 lazyload')
#f4 = f3.find_all('div', 'txt')
print(f3)
for f5 in f4:
    t = f5.find('a')
    print(t)
