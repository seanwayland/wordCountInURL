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


soup2 = BeautifulSoup(html, 'html.parser')

results = []
for x in  soup2.find_all('h3'):
    results.append(x.text)
for y in results:
    if len(y) < 4:
        results.remove(y)
for z in results:
    print(z)




