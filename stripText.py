import urllib
from bs4 import BeautifulSoup
import urllib.request
import itertools
from collections import Counter
import xmltodict

'''
function which strips word from website 
'''
def getWordsFromURL(page):
   # url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
    url = page
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()


    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    #print(text)

    words = text.split()
    words = [x.lower() for x in words]
    return words
''' function which takes a python list of URLS and then returns a list of words in all the websites '''

def getWordsFromUrlList(urlList):
    result = []
    for url in urlList:
        result.append(getWordsFromURL(url))
    ab = itertools.chain(result)
    res =  list(ab)
    return res[0]
'''
function which takes a list of words and returns a dictionary with counts of words sorted 
'''
def getWordCounts(myList):
    counter = Counter(myList)
    occs = [(word,count) for word,count in counter.items()]
    occs.sort(key=lambda x:x[1])
    return occs



urls = ["http://news.bbc.co.uk/2/hi/health/2284783.stm", "https://www.seanwayland.com", "https://www.seanwayland.com/portfolio.html"]
wordList = getWordsFromUrlList(urls)
print(getWordCounts(wordList))



