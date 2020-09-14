from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()


# american eagle
def closeAEPopup():
    button = scraper.browser.find_elements(By.XPATH, '//button[@class="btn-link btn-block clickable reject-cookie-modal-ccpa qa-reject-cookie-modal-ccpa ccpa-accessibility"]')
    try:
        if button:
            button[0].click()
    except:print('button error')
        
pages = ['https://www.ae.com/us/en/c/women/bottoms/jeans/cat6430042?pagetype=plp',
'https://www.ae.com/us/en/c/women/bottoms/joggers-sweatpants/cat7010091?pagetype=plp',
'https://www.ae.com/us/en/c/women/bottoms/pants/cat90034?pagetype=plp',
'https://www.ae.com/us/en/c/women/bottoms/shorts/cat380159?pagetype=plp',
'https://www.ae.com/us/en/c/women/bottoms/leggings/cat200043?pagetype=plp',
'https://www.ae.com/us/en/c/women/bottoms/skirts/cat5920105?pagetype=plp',
'https://www.ae.com/us/en/c/women/tops/t-shirts/cat90030?pagetype=plp',
'https://www.ae.com/us/en/c/women/tops/bodysuits/cat6080084?pagetype=plp',
'https://www.ae.com/us/en/c/women/tops/sweaters-cardigans/cat1410002?pagetype=plp',
'https://www.ae.com/us/en/c/women/dresses/cat1320034?pagetype=plp',
'https://www.ae.com/us/en/c/women/dresses/rompers/cat360011?pagetype=plp']

for page in pages:
    scraper.setURL(page)
    scraper.getProductLinks('//a[@class="xm-link-to qa-xm-link-to tile-link"]', productCount=25, dynamic=True, function=closeAEPopup)
scraper.scrape('American Eagle',  
    '//div[@class="pdp-cap pdp-grid"]/div/h1',
    '//span[@class="equity-item-id equity-item-prod-id"]',
    '//div[@class="equity-group-item equity-group-item-material"]/ul/li[1]',
    '//div[@class="qa-product-prices product-prices __527f1 ember-view"]/div')

scraper.processData('OutputAmericanEagleTest.csv')
scraper.exit()