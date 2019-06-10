from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
#driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
#working one 
#driver.get("https://www.99acres.com/search/property/buy/residential-all/ulwe?search_type=QS&refSection=GNB&search_location=CP12&lstAcn=CP_R&lstAcnId=12&src=CLUSTER&preference=S&selected_tab=1&city=15&res_com=R&property_type=R&isvoicesearch=N&keyword=ulwe&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null")
for i in range(1,10):
    driver = webdriver.Chrome(executable_path=r'C:/Users/vijay/www/webscrap/chromedriver_win32/chromedriver.exe')
    time.sleep(5)
    url ="https://www.99acres.com/property-in-navi-mumbai-ffid-page-{0}?keyword=ulwe".format(i)
    driver.get(url)
    time.sleep(5)
    content = driver.page_source
    soup = BeautifulSoup(content)
    containers = soup.findAll("div",{"class":"srpNw_tble"})
    prices = soup.findAll("span",{"class":"srpNw_price"})


    tables = containers[0].find_all('table')

    R=[]
    S=[]
    

    for container in containers :
        tables = container.find_all('table')
           
        for row in tables[0].findAll("tr"):
            header = row.findAll("th")
            if ( len(header) > 0 ):
                href = (header[0].find("a")).get("href")
                span = header[0].find("span")
                R.append( href )
                S.append( span )
           

    driver.implicitly_wait(5)
    df = pd.DataFrame({'Href':R,'Span':S}) 
    df.to_csv('products.csv', index=False, mode='a',header=False, encoding='utf-8')
    driver.quit()
    time.sleep(5)

'''
df['G']=G
df['H']=H
df['I']=I
df['J']=J
df['K']=K

cells = row.findAll("td")
        R.append(cells)
        if len(cells)==4 :
            #print(cells[0].find(text=True))
            A.append(cells[0].find(text=True))
            B.append(cells[1].find(text=True))
            C.append(cells[2].find(text=True))
            D.append(cells[3].find(text=True))
        
G.append(cells[5].find(text=True))
            H.append(cells[6].find(text=True))
            I.append(cells[7].find(text=True))
            J.append(cells[8].find(text=True))
            K.append(cells[9].find(text=True))

df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capi
   

print(A)

df = pd.DataFrame({'Product Name':containers}) 
df.to_csv('products.csv', index=False, encoding='utf-8')


right_table = containers.find("table")

print (len(right_table))
print ( right_table )

print (len(containers))
print (len(prices))
print (prices[0].text)
titles = soup.findAll("span")
print(len(titles))



for title in titles :
    print (title.get("title"))


for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    
df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
'''
