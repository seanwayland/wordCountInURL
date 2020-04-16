
import urllib.request
import xmltodict
import pprint


'''

SEARCH A URL FOR SITE MAPS 

#############################################
'''

from bs4 import BeautifulSoup
import requests

xmlDict = {}

r = requests.get("http://www.statefarm.com/sitemap.xml")
xml = r.text

soup = BeautifulSoup(xml)
sitemapTags = soup.find_all("sitemap")

print("The number of sitemaps are {0}".format(len(sitemapTags)))

for sitemap in sitemapTags:
    xmlDict[sitemap.findNext("loc").text] = sitemap.findNext("lastmod").text

print(xmlDict)


'''

PRETTY PRINT A YUCKY NESTED OBJECT 
#######################################
'''

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

''' scrape all URLs from sitemap 
##########################################################################'''

file = urllib.request.urlopen('https://www.statefarm.com/sitemap-main.xml')
data = file.read()
file.close()
doc = xmltodict.parse(data)
urlList = []
urls = doc['urlset']['url']
for val in urls:

    urlList.append(val['loc'])
print(urlList)


'''
parse a URL and get the word count 

#######################################

'''


from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

import re
from collections import Counter

combinedlst = []

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    #visible_texts = filter(tag_visible, texts)
    #return u" ".join(t.strip() for t in visible_texts)
    return u" ".join(t.strip() for t in texts)

def parse_html(url):
    html = urllib.request.urlopen(url).read()
    t = (text_from_html(html))
    lst = re.findall(r'\b\w+', t)
    lst = [x.lower() for x in lst]
    for val in lst:
        combinedlst.append(val)

parse_html('https://www.statefarm.com/insurance')

counter = Counter(combinedlst)
occs = [(word,count) for word,count in counter.items() if count > 1]
occs.sort(key=lambda x:x[1])
print(occs)


