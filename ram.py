import urllib.request

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
rt = "https://99acres.com/"
page = urllib.request.urlopen(rt)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page)

print ("hello")

print (soup.title.string)

all_links=soup.find_all("a")

for link in all_links :
    print( link.get("href"))

#print (soup.find_all("a"))


