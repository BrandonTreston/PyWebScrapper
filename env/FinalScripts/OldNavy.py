from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# Old Navy
def triggerOldNavyJS():
    js_string = "document.getElementById('promoBannerMain').remove();"
    scraper.browser.execute_script(js_string)
    js_string2 = "document.getElementsByClassName('brand-bar')[0].remove();"
    scraper.browser.execute_script(js_string2)
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
    js2 = scraper.browser.find_elements(By.XPATH, '//button[@id="product-info-tabs-button--1"][.="Materials & Care"]')
    if js2: js2[0].click()
    sleep(1)

pages = ["https://oldnavy.gap.com/browse/category.do?cid=72091&mlink=5360,1,W_flyout_tops",
'https://oldnavy.gap.com/browse/category.do?cid=15292&nav=leftnav:women:shop%20by%20category:dresses%20',
'https://oldnavy.gap.com/browse/category.do?cid=1051876&nav=leftnav:women:shop%20by%20category:jumpsuits%20%26%20rompers',
'https://oldnavy.gap.com/browse/category.do?cid=1124176&nav=leftnav:women:shop%20by%20category:bottoms',
]
for page in pages:
    scraper.setURL(page)
    scraper.getProductLinks('//div[@class="product-card"]/div/div[@class="product-card__image-wrapper"]/a', productCount=75, dynamic=True)
scraper.scrape('Old Navy',
'//h1[@class="product-title__text"]',
'//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span',
'//div[@id="product-info-tabs-panel--1"]/ul/li[1]/span',
'//div[@class="pdp-pricing"]//h2',
3,
triggerOldNavyJS,
doName=False,
doPrice=False,
doId=False)

scraper.processData('OutputOldNavy.csv')
scraper.exit()