from bs4 import BeautifulSoup
import requests
import urllib
from bs4 import BeautifulSoup
import urllib.request
import itertools
from collections import Counter
#
from htmlpage import page
html = page

soup = BeautifulSoup(html, 'html.parser')

results = []
for x in  soup.find_all('strong'):
    results.append(x.text)
for y in results:
    if len(y) < 4:
        results.remove(y)
for z in results:
    print(z)
    



