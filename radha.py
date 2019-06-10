import time
import io
import csv
import requests
from bs4 import BeautifulSoup
list=[]
for i in range(1, 5):
    time.sleep(5)
    #url = "https://www.99acres.com/3-bhk-property-in-hyderabad-ffid-page-{0}".format(i)
    url ="https://www.99acres.com/property-in-navi-mumbai-ffid-page-{0}?keyword=ulwe".format(i)

    response = requests.get(url)
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')


    dealer = soup.findAll('div',{'class': 'srpWrap'})

    for item in dealer:
        try:
            p = item.contents[1].find_all("div",{"class":"_srpttl srpttl fwn wdthFix480 lf"})[0].text
        except:
            p=''
        try:
            d = item.contents[1].find_all("div",{"class":"lf f13 hm10 mb5"})[0].text
        except:
            d=''

        li=[p,d]
        list.append(li)


    with open('project.txt','w',encoding="utf-8") as file:
        writer= csv.writer(file)
        for row in list:
            writer.writerows(row)

    file.close()
