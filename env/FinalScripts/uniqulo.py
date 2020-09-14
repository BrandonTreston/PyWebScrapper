from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()


# uniqulo
def closeUniPopup():
    button = scraper.browser.find_elements(By.XPATH, '//a[@id="bx-close-inside-1189401"]')
    try:
        if button:
            button[0].click()
    except:
        print('button error')
        
def showMaterials():
    try:
        js_string = "document.getElementById('covid-footer').remove();"
        scraper.browser.execute_script(js_string)
        button = scraper.browser.find_elements(By.XPATH, '//button[@id="tab-meterials-care"]')
        if button:
            button[0].click()
    except:print('showMaterials error')

pages = ['https://www.uniqlo.com/us/en/women/dresses-and-jumpsuits',
'https://www.uniqlo.com/us/en/women/t-shirts-and-tops',
'https://www.uniqlo.com/us/en/women/sweaters-and-cardigans',
'https://www.uniqlo.com/us/en/women/skirts',
'https://www.uniqlo.com/us/en/women/shorts',
'https://www.uniqlo.com/us/en/women/jeans',
'https://www.uniqlo.com/us/en/women/pants']

for page in pages:
    scraper.setURL(page)
    scraper.getProductLinks('//div[@class="hover-wrapper"]/div/a', productCount=30, function=closeUniPopup, dynamic=True)
scraper.scrape('Uniqulo',
'//span[@class="product-name"]',
'//span[@class="breadcrumb-productid"]',
'//ul[@class="prodspec"]/li[contains(.,"%")]',
'//span[@itemprop="price"]',
function=showMaterials)

scraper.processData('OutputUniqulo.csv')
scraper.exit()