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
#for i in range(1,2):
i=1
driver = webdriver.Chrome(executable_path=r'C:/Users/vijay/www/webscrap/chromedriver_win32/chromedriver.exe')
#time.sleep(1)
url ="https://www.99acres.com/property-in-navi-mumbai-ffid-page-{0}?keyword=ulwe".format(i)
driver.get(url)
#time.sleep(2)
content = driver.page_source
soup = BeautifulSoup(content)
containers = soup.findAll("div",{"class":"srpNw_tble"})
prices = soup.findAll("span",{"class":"srpNw_price"})


tables = containers[0].find_all('table')

header_href=[]
header_span=[]
td_prices=[]

for container in containers :
    tables = container.find_all('table')
       
    for row in tables[0].findAll("tr"):
        header = row.findAll("th")
        td_price = row.findAll("tr",{"class":"_auto_bedroom"})
        td_areaValue = row.findAll("tr",{"class":"_auto_areaValue"})
        td_possesion = row.findAll("tr",{"class":"_auto_possesionLabel"})
        td_ppu_area = row.findAll("tr",{"class":"_auto_ppu_area"})
        td_areaType = row.findAll("tr",{"class":"_auto_areaType"})
        td_bath_balc = row.findAll("tr",{"class":"_auto_bath_balc_roadText"})
        td_desc = row.findAll("div",{"class":"srpNw_desc __srpNw_desc"})
        td_price = row.findAll("span",{"class":"srpNw_price"})
        
        td_prices.append(td_price)
        if ( len(header) > 0 ):
            href = (header[0].find("a")).get("href")
            span = header[0].find("span")
            header_href.append( href )
            header_span.append( span )
       

driver.implicitly_wait(5)
df = pd.DataFrame({'Href':header_href,'Span':header_span,'Price':td_prices}) 
df.to_csv('products.csv', index=False, mode='a',header=False, encoding='utf-8')
driver.quit()
#time.sleep(5)

'''
df.to_csv('products.csv', index=False, encoding='utf-8')
'''
