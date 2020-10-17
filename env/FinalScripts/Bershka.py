from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# Bershka
def bershkaJS():
    button = scraper.browser.find_elements(By.XPATH, '//li[@id="compositionLink"]/span[@class="product-description-moreinfo-text"]')
    try:
        if button:
            button[0].click()
            sleep(2)
    except:
        print('button error')

def showMoreProducts():
    button= scraper.browser.find_elements(By.XPATH, '//div[@class="grid-size-selector"]/ul/li[@class="view-6-link greyHover view-element"]/a[@class="view-element-link"]')
    if button:
        button[0].click()
        sleep(2)

pages = ['https://www.bershka.com/us/women/collection/pants-c1010193216.html',
'https://www.bershka.com/us/women/collection/jeans-c1010276029.html',
'https://www.bershka.com/us/women/collection/dresses-c1010193213.html',
'https://www.bershka.com/us/women/collection/skirts-c1010193224.html',
'https://www.bershka.com/us/women/collection/shorts-and-bermudas-c1010194517.html',
'https://www.bershka.com/us/women/collection/tees-c1010193217.html',
'https://www.bershka.com/us/women/collection/tops-c1010193220.html',
'https://www.bershka.com/us/women/collection/bodysuits-c1010193219.html',
'https://www.bershka.com/us/women/collection/sweatshirts-and-hoodies-c1010193222.html']

for page in pages:
    scraper.setURL(page)
    scraper.getProductLinks('//div/a[@class="grid-card-link"]', productCount= 30, dynamic=True, function=showMoreProducts)
scraper.scrape(
    'Bershka',
    '//h1[@class="product-title"]',
    '//div[@class="product-reference"]',
    '//section[@class="about-product"]/section[@class="product-compositions"]',
    '//div[@class="current-price-elem"]',
    function = bershkaJS,
    delay= 15)

scraper.processData('OutputBershka.csv')
scraper.exit()