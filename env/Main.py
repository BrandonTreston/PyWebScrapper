from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By

scraper = Scraper()

# #H&M
scraper.setURL('https://www2.hm.com/en_us/women/products/view-all.html?sort=stock&productTypes=Blazer,Blouse,Body,Cardigan,Coat,Dress,Jacket,Jeans,Jumper,Jumpsuit,Leggings,Pants,Shirt,Shorts,Skirt,T-shirt,Top&image-size=small&image=model&offset=0&page-size=250')
scraper.getProductLinks('//h3[@class="item-heading"]//a[@class="link"]', pages=0, productCount=250)
scraper.scrape('H&M',
'//h1[@class="primary product-item-headline"]',
'//dl[@class="pdp-description-list"]/div/dt[text()="Art. No."]//following-sibling::dd',
'//dl[@class="pdp-description-list"]/div/dt[text()="Composition"]//following-sibling::dd',
'//span[@class="price-value"]'
)

# american apparel
def closeAPPopUp():
    closeButton = scraper.browser.find_elements(By.XPATH, '//img[@aria-label="Popup Close Button"]')[0]
    if closeButton:
        closeButton.click()

def getPrice():
    price = scraper.browser.find_elements(By.XPATH, '//div[@class="amazon-link"]/a')[0].get_property('href')
    scraper.setURL(price)
    price = scraper.browser.find_elements(By.XPATH, '//div[@id="price"]/table/tbody/tr/td[2]/span')[0].text
    scraper.price.append(price)
    scraper.browser.back()

scraper.setURL("https://americanapparel.com/women/?_bc_fsnf=1&Product+Type%5B%5D=Bodysuits&Product+Type%5B%5D=Camis&Product+Type%5B%5D=Cardigans&Product+Type%5B%5D=Dresses&Product+Type%5B%5D=Hoodies&Product+Type%5B%5D=Jackets&Product+Type%5B%5D=Jeans&Product+Type%5B%5D=Joggers&Product+Type%5B%5D=Jumpsuits&Product+Type%5B%5D=Leggings&Product+Type%5B%5D=Pants&Product+Type%5B%5D=Shorts&Product+Type%5B%5D=Skirts&Product+Type%5B%5D=Sweaters&Product+Type%5B%5D=Sweatshirts&Product+Type%5B%5D=T-Shirts")
scraper.getProductLinks('//a[@class="plp-product-link"]',0, 250, paginated=False, dynamic=True,)
scraper.scrape('American Apparel',
'//h1[@class="productView-title"]',
'//dd[@class="productView-info-value"]',
'//div[@class="product-fabric-details"]//div[2]//div[1]//p[2]',
'//div[@class="price-does-not-exist"]',
function=getPrice)

# GAP
def closeGapPopUp():
    scraper.links.append('https://www.gap.com/browse/OutOfStockNoResults.do?pid=583592002&cid=1127938&pcid=1127938&vid=1&grid=pds_193_2454_1&cpos=193&cexp=1488&kcid=CategoryIDs%3D1127938&ctype=Listing&cpid=res20073118398562901373283&requestedurl=www.gap.com%2Fbrowse%2Fproduct.do%3Fpid%3D583592002%26cid%3D1127938%26pcid%3D1127938%26vid%3D1%26grid%3Dpds_193_2454_1%26cpos%3D193%26cexp%3D1488%26kcid%3DCategoryIDs%253D1127938%26ctype%3DListing%26cpid%3Dres20073118398562901373283')
    closePopUpButton = scraper.browser.find_elements(By.XPATH, '//button[@class="css-1qosac6"]')[0]
    if closePopUpButton:
        closePopUpButton.click()
    js_string = "document.getElementById('promoBannerMain').remove();"
    scraper.browser.execute_script(js_string)
    #scroll page to load dynamic content
    i = 0
    while i < 5000:
        scraper.browser.execute_script("window.scrollBy(0,10);")
        i += 1
    scraper.browser.execute_script("window.scrollTo(0,0);")
    offset = scraper.browser.find_element(By.XPATH, '//button[@class="css-1kxwv5e"]')
    scraper.browser.execute_script("arguments[0].scrollIntoView();", offset)

def triggerGapJS():
    js_string = "document.getElementById('promoBannerMain').remove();"
    scraper.browser.execute_script(js_string)
    try:
        name = scraper.browser.find_elements(By.XPATH, '//h1[@class="product-title__text"]')[0]
        price = scraper.browser.find_elements(By.XPATH, '//div[@class="pdp-pricing"]//h2')[0]
    except:
        name = ''
        price = ''
    if name:
        scraper.product_name.append(name.text)
        scraper.price.append(price.text)
        scraper.getType(name.text)
    try:
        js = scraper.browser.find_elements(By.XPATH, '//button[@class="pdp-drawer-trigger"]')[0]
        js.click()
        id = scraper.browser.find_elements(By.XPATH, '//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span')[0]
        if id: scraper.product_id.append(id.text)
        js2 = scraper.browser.find_elements(By.XPATH, '//button[@id="product-info-tabs-button--1"][.="fabric & care"]')[0]
        js2.click()
    except:
        id = ''


scraper.setURL('https://www.gap.com/browse/category.do?cid=1127938#pageId=0&department=136&nav=leftnav:women:categories')
scraper.getProductLinks('//div[@class="product-card"]/a[@class="product-card__link"]', pages=1, productCount=299, buttonSelector='//nav[@class="css-1l418ga-Paginator"]/button[@aria-label="Next Page"]', function=closeGapPopUp, paginated=True, dynamic=False)
scraper.scrape('GAP',
'//h1[@class="product-title__text"]',
'//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span',
'//div[@id="product-info-tabs-panel--1"]/ul/li[1]/span',
'//div[@class="pdp-pricing"]//h2',
3,
triggerGapJS)

scraper.processData('outputFinal.csv')
scraper.exit()