# RUN pip install bs4
# RUN pip install lxml
# RUN pip install requests

import bs4
import lxml
import requests

links = []
def scrap(url='https://yoursite.com'):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    link = soup.find_all('a', href=True)
    for l in link:
        if l not in links:
            links.append(l['href'])

    clean()

def clean():
    i = 0
    for items in links:
        if items.startswith('http'):
            del links[i]
        if not items.startswith('https://yoursite.com'):
            del links[i]
            i += 1

scrap()

print(links)
