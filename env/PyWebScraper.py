from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
from datetime import datetime
import pandas as pd

options = Options()
options.headless = True
path = 'chromedriver.exe'
browser = webdriver.Chrome(path) #pass options as second argument to run browser without gui

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

#load dynamic content by scrolling to bottom of page    
def getProductLinks(productSelector, pages=0, productCount=10, paginated=False, buttonSelector=''):
    """Gets a list of all web elements containing links to the individual product pages

    Parameters
    ----------
    productSelector : str
        string containing XPATH find product links
    pages : str (optional)
        number of pages containing product links
    productCount : int (optional)
        Number of products to scrape. Defaults to 250. It is reccomended to use this parameter to limit the number of items to be scraped if desired.
    paginated : bool (optional)
        Tells the scraper if the catalog is paginated. If true, the scraper will navigate between those pages.
    buttonSelector : str (optional)
        Tells the scraper the xpath for the element that will send the scraper to the next page, avoiding complicated URL manipulation for each site.
    """
    elements = []
    for i in range(0,5):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

    if paginated == True:
        for page in range(0,pages):
            #find all product links. returns list, stores at elements.
            _elements = (browser.find_elements(By.XPATH, productSelector))
            for element in _elements:
                elements.append(element)
            browser.find_elements(By.XPATH, buttonSelector).click()     
    else:
        _elements = (browser.find_elements(By.XPATH, productSelector))
        for element in _elements:
                elements.append(element)
    #slice the list if it exceeds the range
    if len(elements) > productCount:
        elements = elements[:productCount]

    for we in elements:
        #get the href attribute of each web element in elements
        links.append(we.get_property('href'))

def scrape(brandName, nameSelector, idSelector, compositionSelector, priceSelector, delay=3):
    """Visits each link and scrapes the page using provided XPATH parameters.

    Parameters
    ----------
    brandName : str
        Name of brand from which the article of clothing is from.
    nameSelector : str
        XPATH string for XML/HTML web element containing productg name.
    idSelector: str
        String containing XPATH for the product id web element
    compositionSelector : str
        String containing XPATH for the composition web element
    priceSelector : str
        String containing XPATH for the price web element
    delay : int (optional)
        Sets the delay to scrape each product, as specified in a site's robots.txt file. Defaults to 3 seconds.
    """
    for link in links:
        browser.get(link)
        sleep(delay)
       
        # #scrape web elements containing desired data: temporary storage
        _brand = brandName
        name = browser.find_elements(By.XPATH, nameSelector)
        _id = browser.find_elements(By.XPATH, idSelector)
        composition = browser.find_elements(By.XPATH, compositionSelector)
        title = browser.title
        _price = browser.find_elements(By.XPATH, priceSelector)
        extraction_time.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

        #check if data exists after scraping, add it to data store if so
        if _brand:
            brand.append(_brand)
        if name:
            product_name.append(name[0].text)
        if _id:
            product_id.append(_id[0].text)
        if composition:
            properties.append(composition[0].text)
        else:
            properties.append("n/a")
        if title:
            page_title.append(title)
        if _price:
            price.append(_price[0].text)
        else:
            price.append('n/a')

        #determine product type by its name
        getType(name[0].text)

def getType(productInput):
    """Checks product name for keywords to determine basic article type.

    Parameters
    ----------
    productName : str
        String containing the product name.
    """
    productName = productInput.lower()
    type = ''
    if 'shirt' in productName or 'top' in productName or 'blouse' in productName or 'tee' in productName or 'cami' in productName:
        type = 'top'
    elif 'hood' in productName or 'jacket' in productName or 'sweatshirt' in productName or 'sweater' in productName or 'cardigan' in productName or 'pullover' in productName:
        type = 'outterwear/jacket'
    elif 'jean' in productName or 'jogger' in productName or 'legging' in productName or 'pant' in productName or 'skirt' in productName or 'short' in productName:
        type = 'bottoms'
    elif 'dress' in productName:
        type = 'dress'
    elif 'romper' in productName or 'bodysuit' in productName or 'jump' in productName or 'suit' in productName or 'coverall' in productName:
        type = 'bodysuit/romper'
    else:
        type = 'other'
    product_description.append(type)

def processData():
    """Create a dataframe for the data gathered by the scrape() method."""
    articles = pd.DataFrame({
        'Brand' : brand,
        'Name': product_name,
        'Type': product_description,
        'ID': product_id,
        'Composition': properties,
        'Time of Extraction': extraction_time,
        'PageTitle': page_title,
        'Price': price
    })
    articles.to_csv('output2.csv')

def clearLinks():
    links = [] #clear links for next site

#product catalog url
url = "https://www2.hm.com/en_us/women/products/view-all.html?sort=stock&productTypes=Blazer,Blouse,Body,Cardigan,Coat,Dress,Jacket,Jeans,Jumper,Jumpsuit,Leggings,Pants,Shirt,Shorts,Skirt,T-shirt,Top&image-size=small&image=model&offset=0&page-size=250"
browser.get(url)
#let page load for 4 seconds
sleep(4)
getProductLinks('//h3[@class="item-heading"]//a[@class="link"]')
scrape('H&M',
'//h1[@class="primary product-item-headline"]',
'//dl[@class="pdp-description-list"]/div/dt[text()="Art. No."]/following-sibling::dd',
'//dl[@class="pdp-description-list"]/div/dt[text()="Composition"]/following-sibling::dd',
'//span[@class="price-value"]'
)

url = "https://americanapparel.com/women/?_bc_fsnf=1&Product+Type%5B%5D=Bodysuits&Product+Type%5B%5D=Camis&Product+Type%5B%5D=Cardigans&Product+Type%5B%5D=Dresses&Product+Type%5B%5D=Hoodies&Product+Type%5B%5D=Jackets&Product+Type%5B%5D=Jeans&Product+Type%5B%5D=Joggers&Product+Type%5B%5D=Jumpsuits&Product+Type%5B%5D=Leggings&Product+Type%5B%5D=Pants&Product+Type%5B%5D=Shorts&Product+Type%5B%5D=Skirts&Product+Type%5B%5D=Sweaters&Product+Type%5B%5D=Sweatshirts&Product+Type%5B%5D=T-Shirts"
browser.get(url)
getProductLinks('//a[@class="plp-product-link"]')
scrape('American Apparel',
'//h1[@class="productView-title"]',
'//dd[@class="productView-info-value"]',
'//div[@class="product-fabric-details"]/div[2]/div[1]/p[2]',
'//div[@class="price-does-not-exist"]')

processData()

#close the browser
browser.quit()
print('done.')