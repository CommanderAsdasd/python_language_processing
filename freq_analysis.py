import requests
import nltk
import re
from collections import Counter
c = Counter("Hello")
print(c.most_common())

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


r = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
text = cleanhtml(r.text)
text = text.split(" ")
# print(text.)
# print(text.count("the"))
fd = nltk.FreqDist(text)
print(fd.most_common())
fd.plot(10) 