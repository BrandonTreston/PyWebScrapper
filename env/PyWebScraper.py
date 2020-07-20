from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
from datetime import datetime

options = Options()
options.headless = True
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

headers = {"Accept-Language": "en-US,en;q=0.5"}

#data storage
brand = []
product_name = []
product_description = []
product_id = []
price = []
properties = []
page_title = []
extraction_time = []

#links for each product
links = []

#for dynamic non paginated catalogs
paginated = False
dynamic = True
url = 'https://americanapparel.com/women/?_bc_fsnf=1&Product+Type%5B%5D=Bodysuits&Product+Type%5B%5D=Camis&Product+Type%5B%5D=Cardigans&Product+Type%5B%5D=Dresses&Product+Type%5B%5D=Hoodies&Product+Type%5B%5D=Jackets&Product+Type%5B%5D=Jeans&Product+Type%5B%5D=Joggers&Product+Type%5B%5D=Jumpsuits&Product+Type%5B%5D=Leggings&Product+Type%5B%5D=Pants&Product+Type%5B%5D=Shorts&Product+Type%5B%5D=Skirts&Product+Type%5B%5D=Sweaters&Product+Type%5B%5D=Sweatshirts&Product+Type%5B%5D=T-Shirts'

browser.get(url)
sleep(5)


#load dynamic content by scrolling to bottom of page    
for i in range(0,5):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)
        
    #find all product links, get the value, store in links.
    elements = browser.find_elements(By.XPATH, '//a[@class="plp-product-link"]')
for we in elements:
    links.append(we.get_property('href'))

for link in links:
    browser.get(link)
    sleep(3)
    #scrape webelements containing desired data
    _brand = "American Apperal" #brand
    name = browser.find_elements(By.XPATH, '//h1[@class="productView-title"]') #name
    description = browser.find_elements(By.XPATH, '//div[@class="productView-product"]/div[1]') #description
    _id = browser.find_elements(By.XPATH, '//dd[@class="productView-info-value"]') #id
    # _price = browser.find_elements() #price
    composition = browser.find_elements(By.XPATH, '//div[@class="custom-collapsible-content product-fabric-details-content is-open"]/div[1]/p[2]') #composition string
    title = browser.find_elements_by_tag_name('title') #html page title
    extraction_time.append(datetime.now().strftime("%M/%D/%Y, %H:%M:%S")) #extraction time

    #check if data exists after scraping, add it to data store if so
    if _brand:
        brand.append(_brand[0])
    if name:
        print(name[0].text)
        product_name.append(name[0].text)
    if description:
        print(description[0].text)
        product_description.append(description[0].text)
    #if _price:
        #price.append(_price[0].text)    
    if composition:
        print(composition[0].text)
        properties.append(composition[0].text)
    if title:
        print(title[0].text)
        page_title.append(title[0].text) 


#close the browser
browser.quit()
