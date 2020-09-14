from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# american apparel
def closeAPPopUp():
    closeButton = scraper.browser.find_elements(By.XPATH, '//img[@aria-label="Popup Close Button"]')[0]
    try:
        if closeButton:
            closeButton.click()
    except:
        print('button error')
def getPrice():
    try:
        price = scraper.browser.find_elements(By.XPATH, '//div[@class="amazon-link"]/a')[0].get_property('href')
        scraper.setURL(price)
        price = scraper.browser.find_elements(By.XPATH, '//div[@id="price"]/table/tbody/tr/td[2]/span')
        if price:
            scraper.price.append(price[0].text)
            scraper.browser.back()
        else:
            scraper.price.append(' ')
            scraper.browser.back()
    except: print('getPrice error')
scraper.setURL("https://americanapparel.com/women/?_bc_fsnf=1&Product+Type%5B%5D=Bodysuits&Product+Type%5B%5D=Camis&Product+Type%5B%5D=Cardigans&Product+Type%5B%5D=Dresses&Product+Type%5B%5D=Hoodies&Product+Type%5B%5D=Jackets&Product+Type%5B%5D=Jeans&Product+Type%5B%5D=Joggers&Product+Type%5B%5D=Jumpsuits&Product+Type%5B%5D=Leggings&Product+Type%5B%5D=Pants&Product+Type%5B%5D=Shorts&Product+Type%5B%5D=Skirts&Product+Type%5B%5D=Sweaters&Product+Type%5B%5D=Sweatshirts&Product+Type%5B%5D=T-Shirts")
scraper.getProductLinks('//a[@class="plp-product-link"]',0, 250, paginated=False, dynamic=True,)
scraper.scrape('American Apparel',
'//h1[@class="productView-title"]',
'//dd[@class="productView-info-value"]',
'//div[@class="product-fabric-details"]//div[2]//div[1]//p[2]',
'//div[@class="price-does-not-exist"]',
function=getPrice,
doPrice=False)

scraper.processData('OutputAmericanApparel.csv')
scraper.exit()