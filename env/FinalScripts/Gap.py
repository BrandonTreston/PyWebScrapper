from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# GAP
def closeGapPopUp():
    closePopUpButton = scraper.browser.find_elements(By.XPATH, '//button[@class="css-1qosac6"]')
    if closePopUpButton:
        closePopUpButton[0].click()
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
    sleep(1)
    price = scraper.browser.find_elements(By.XPATH, '//div[@class="pdp-pricing"]//h2')
    if price: scraper.price.append(price[0].text)
    else: scraper.price.append(' ')
    name = scraper.browser.find_elements(By.XPATH, '//h1[@class="product-title__text"]')
    if name: 
        scraper.product_name.append(name[0].text)
        scraper.getType(name[0].text)
    else:
        scraper.product_name.append(' ')
        scraper.product_description.append(' ')
    js = scraper.browser.find_elements(By.XPATH, '//button[@class="pdp-drawer-trigger"]')
    if js: js[0].click()
    sleep(1)
    id = scraper.browser.find_elements(By.XPATH, '//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span')
    if id: scraper.product_id.append(id[0].text)
    else: scraper.product_id.append(' ')
    scraper.browser.execute_script("window.scrollTo(0,0);")
    js2 = scraper.browser.find_elements(By.XPATH, '//button[@id="product-info-tabs-button--1"][.="fabric & care"]')
    if js2: js2[0].click()
    sleep(1)

scraper.setURL('https://www.gap.com/browse/category.do?cid=1127938#pageId=0&department=136&nav=leftnav:women:categories')
scraper.getProductLinks('//div[@class="product-card"]/a[@class="product-card__link"]', pages=1, productCount=300, buttonSelector='//nav[@class="css-1l418ga-Paginator"]/button[@aria-label="Next Page"]', function=closeGapPopUp, paginated=True)
scraper.scrape('GAP',
'//h1[@class="product-title__text"]',
'//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span',
'//div[@id="product-info-tabs-panel--1"]/ul/li[1]/span',
'//div[@class="pdp-pricing"]//h2',
3,
triggerGapJS,
doName=False,
doPrice=False,
doId=False)

scraper.processData('OutputGap.csv')
scraper.exit()