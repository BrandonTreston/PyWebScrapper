from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# Reformation
def trigerHomepage():
    sleep(1)
    button = scraper.browser.find_elements(By.XPATH, '//button[@data-browse-view-options="4"]')
    try:
        if button:
            button[0].click()
    except:
        print('button error')
def getID():
    try:
        id = scraper.browser.find_elements(By.XPATH, '//meta[@itemprop="sku"]')
        if id:
            scraper.product_id.append(id[0].get_property('content'))
        else: scraper.product_id.append(" ")
        button = scraper.browser.find_elements(By.XPATH, '//div[@aria-label="Fabric & care"]')
        if button:
            button[0].click()
    except:
        print('getID error')
def triggerProductJS():
    try:
        check = scraper.browser.find_elements(By.XPATH, '//img')
        if not check:
            sleep(20) #reformation sometimes doesn't load the page saying to retry. This checks for that and waits to retry
            scraper.browser.refresh()
            getID()
        else:
            getID() 
    except:print('JS error')
scraper.setURL('https://www.thereformation.com/categories/shop?types%5B%5D=Bodysuit&types%5B%5D=Jeans&types%5B%5D=Long+Dresses&types%5B%5D=Long+Jumpsuits&types%5B%5D=Midi+Dresses&types%5B%5D=Pants&types%5B%5D=Short+Dresses&types%5B%5D=Shorts&types%5B%5D=Skirts&types%5B%5D=Sweaters&types%5B%5D=Tees')
scraper.getProductLinks('//div[@class="product-grid__cell"]/div/div/a[@class="product-summary__media-link"]', productCount=230, dynamic=True, function=trigerHomepage)
scraper.scrape('Reformation',
'//h1[@class="pdp__name"]',
'//div[@class="doesnotexist"]',
'//ul[@class="pdp-product-data"]/li[contains(., "%")]',
'//p[@class="product-prices__price"]/span',
function=triggerProductJS,
delay= 10,
doId=False
)

scraper.processData('OutputReformation.csv')
scraper.exit()