from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# # H&M
# scraper.setURL('https://www2.hm.com/en_us/women/products/view-all.html?sort=stock&productTypes=Blazer,Blouse,Body,Cardigan,Coat,Dress,Jacket,Jeans,Jumper,Jumpsuit,Leggings,Pants,Shirt,Shorts,Skirt,T-shirt,Top&image-size=small&image=model&offset=0&page-size=250')
# scraper.getProductLinks('//h3[@class="item-heading"]//a[@class="link"]', pages=0, productCount=250)
# scraper.scrape('H&M',
# '//h1[@class="primary product-item-headline"]',
# '//dl[@class="pdp-description-list"]/div/dt[text()="Art. No."]//following-sibling::dd',
# '//dl[@class="pdp-description-list"]/div/dt[text()="Composition"]//following-sibling::dd',
# '//span[@class="price-value"]'
# )

# # american apparel
# def closeAPPopUp():
#     closeButton = scraper.browser.find_elements(By.XPATH, '//img[@aria-label="Popup Close Button"]')[0]
#     if closeButton:
#         closeButton.click()

# def getPrice():
#     price = scraper.browser.find_elements(By.XPATH, '//div[@class="amazon-link"]/a')[0].get_property('href')
#     scraper.setURL(price)
#     price = scraper.browser.find_elements(By.XPATH, '//div[@id="price"]/table/tbody/tr/td[2]/span')[0].text
#     scraper.price.append(price)
#     scraper.browser.back()

# scraper.setURL("https://americanapparel.com/women/?_bc_fsnf=1&Product+Type%5B%5D=Bodysuits&Product+Type%5B%5D=Camis&Product+Type%5B%5D=Cardigans&Product+Type%5B%5D=Dresses&Product+Type%5B%5D=Hoodies&Product+Type%5B%5D=Jackets&Product+Type%5B%5D=Jeans&Product+Type%5B%5D=Joggers&Product+Type%5B%5D=Jumpsuits&Product+Type%5B%5D=Leggings&Product+Type%5B%5D=Pants&Product+Type%5B%5D=Shorts&Product+Type%5B%5D=Skirts&Product+Type%5B%5D=Sweaters&Product+Type%5B%5D=Sweatshirts&Product+Type%5B%5D=T-Shirts")
# scraper.getProductLinks('//a[@class="plp-product-link"]',0, 250, paginated=False, dynamic=True,)
# scraper.scrape('American Apparel',
# '//h1[@class="productView-title"]',
# '//dd[@class="productView-info-value"]',
# '//div[@class="product-fabric-details"]//div[2]//div[1]//p[2]',
# '//div[@class="price-does-not-exist"]',
# function=getPrice)

# # GAP
# def closeGapPopUp():
#     closePopUpButton = scraper.browser.find_elements(By.XPATH, '//button[@class="css-1qosac6"]')
#     if closePopUpButton:
#         closePopUpButton[0].click()
#     js_string = "document.getElementById('promoBannerMain').remove();"
#     scraper.browser.execute_script(js_string)
#     #scroll page to load dynamic content
#     i = 0
#     while i < 5000:
#         scraper.browser.execute_script("window.scrollBy(0,10);")
#         i += 1
#     scraper.browser.execute_script("window.scrollTo(0,0);")
#     offset = scraper.browser.find_element(By.XPATH, '//button[@class="css-1kxwv5e"]')
#     scraper.browser.execute_script("arguments[0].scrollIntoView();", offset)

# def triggerGapJS():
#     js_string = "document.getElementById('promoBannerMain').remove();"
#     scraper.browser.execute_script(js_string)
#     sleep(1)
#     price = scraper.browser.find_elements(By.XPATH, '//div[@class="pdp-pricing"]//h2')
#     if price: scraper.price.append(price[0].text)
#     else: scraper.price.append(' ')
#     name = scraper.browser.find_elements(By.XPATH, '//h1[@class="product-title__text"]')
#     if name: 
#         scraper.product_name.append(name[0].text)
#         scraper.getType(name[0].text)
#     else:
#         scraper.product_name.append(' ')
#         scraper.product_description.append(' ')
#     js = scraper.browser.find_elements(By.XPATH, '//button[@class="pdp-drawer-trigger"]')
#     if js: js[0].click()
#     sleep(1)
#     id = scraper.browser.find_elements(By.XPATH, '//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span')
#     if id: scraper.product_id.append(id[0].text)
#     else: scraper.product_id.append(' ')
#     scraper.browser.execute_script("window.scrollTo(0,0);")
#     js2 = scraper.browser.find_elements(By.XPATH, '//button[@id="product-info-tabs-button--1"][.="fabric & care"]')
#     if js2: js2[0].click()
#     sleep(1)

# scraper.setURL('https://www.gap.com/browse/category.do?cid=1127938#pageId=0&department=136&nav=leftnav:women:categories')
# scraper.getProductLinks('//div[@class="product-card"]/a[@class="product-card__link"]', pages=1, productCount=300, buttonSelector='//nav[@class="css-1l418ga-Paginator"]/button[@aria-label="Next Page"]', function=closeGapPopUp, paginated=True, dynamic=False)
# scraper.scrape('GAP',
# '//h1[@class="product-title__text"]',
# '//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span',
# '//div[@id="product-info-tabs-panel--1"]/ul/li[1]/span',
# '//div[@class="pdp-pricing"]//h2',
# 3,
# triggerGapJS)

#american eagle
# def closeAEPopup():
#     button = scraper.browser.find_elements(By.XPATH, '//button[@class="btn-link btn-block clickable reject-cookie-modal-ccpa qa-reject-cookie-modal-ccpa ccpa-accessibility"]')
#     if button:
#         button[0].click()
# pages = ['https://www.ae.com/us/en/c/women/bottoms/jeans/cat6430042?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/bottoms/joggers-sweatpants/cat7010091?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/bottoms/pants/cat90034?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/bottoms/shorts/cat380159?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/bottoms/leggings/cat200043?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/bottoms/skirts/cat5920105?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/tops/t-shirts/cat90030?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/tops/bodysuits/cat6080084?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/tops/sweaters-cardigans/cat1410002?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/dresses/cat1320034?pagetype=plp',
# 'https://www.ae.com/us/en/c/women/dresses/rompers/cat360011?pagetype=plp']

# for page in pages:
#     scraper.setURL(page)
#     scraper.getProductLinks('//div[@class="product-tile qa-product-tile __eadf2 ember-view col-md-3 col-xs-6"]/a', productCount=25, dynamic=True, function=closeAEPopup)
#     print(len(scraper.links))
#     scraper.scrape(
#         'American Eagle',  
#         '//h1[@class="product-name"]',
#         '//span[@class="equity-item-id equity-item-prod-id"]',
#         '//div[@class="equity-group-item equity-group-item-material"]/ul/li[1]',
#         '//div[@class="qa-product-prices product-prices __527f1 ember-view"]/div'
#     )

#Bershka
# def bershkaJS():
#     button = scraper.browser.find_elements(By.XPATH, '//li[@id="compositionLink"]/span[@class="product-description-moreinfo-text"]')
#     if button:
#         button[0].click()
#         sleep(2)

# def showMoreProducts():
#     button= scraper.browser.find_elements(By.XPATH, '//div[@class="grid-size-selector"]/ul/li[@class="view-6-link greyHover view-element"]/a[@class="view-element-link"]')
#     if button:
#         button[0].click()
#         sleep(2)

# pages = ['https://www.bershka.com/us/women/collection/pants-c1010193216.html',
# 'https://www.bershka.com/us/women/collection/jeans-c1010276029.html',
# 'https://www.bershka.com/us/women/collection/dresses-c1010193213.html',
# 'https://www.bershka.com/us/women/collection/skirts-c1010193224.html',
# 'https://www.bershka.com/us/women/collection/shorts-and-bermudas-c1010194517.html',
# 'https://www.bershka.com/us/women/collection/tees-c1010193217.html',
# 'https://www.bershka.com/us/women/collection/tops-c1010193220.html',
# 'https://www.bershka.com/us/women/collection/bodysuits-c1010193219.html',
# 'https://www.bershka.com/us/women/collection/sweatshirts-and-hoodies-c1010193222.html']

# for page in pages:
#     scraper.setURL(page)
#     scraper.getProductLinks('//div[@class="image"]/a', productCount= 30, dynamic=True, function=showMoreProducts)
#     scraper.scrape(
#         'Bershka',
#         '//h1[@class="product-description-name"]',
#         '//div[@class="product-info-elements"]/p[@class="product-detail-reference"]',
#         '//div[@id="modal"]/div/div/div[@class="composition-by-zone-container"][1]/div[@class="composition-by-zone-compositions"]/p',
#         '//span[@class="product-price prices"]/span',
#         function = bershkaJS
#     )

# # Forever21
# def closeF21Popup():
#     sleep(11) #wait for popup's close button to appear
#     button = scraper.browser.find_elements(By.XPATH, '//a[@id="bx-close-inside-1198041"]')
#     if button:
#         button[0].click()

# scraper.setURL('https://www.forever21.com/us/shop/catalog/category/f21/app-main')
# scraper.getProductLinks('//a[@class="item_slider product_link"]', buttonSelector='//span[@class="p_next"]', paginated=True, productCount=250, pages=5, function=closeF21Popup )
# scraper.scrape('Forever 21',
# '//h1[@id="h1Title"]',
# '//div[@id="tabDescriptionContent"]/span[@class="t_mid pt_10"]',
# '//div[@id="divDescription"]/section[2]/div/p[contains(., "%")]',
# '//div[@id="ItemPrice"]/div/span'
# )

# #Old Navy
# def triggerOldNavyJS():
#     js_string = "document.getElementById('promoBannerMain').remove();"
#     scraper.browser.execute_script(js_string)
#     sleep(1)
#     price = scraper.browser.find_elements(By.XPATH, '//div[@class="pdp-pricing"]//h2')
#     if price: scraper.price.append(price[0].text)
#     name = scraper.browser.find_elements(By.XPATH, '//h1[@class="product-title__text"]')
#     if name: 
#         scraper.product_name.append(name[0].text)
#         scraper.getType(name[0].text)
#     js = scraper.browser.find_elements(By.XPATH, '//button[@class="pdp-drawer-trigger"]')
#     if js: js[0].click()
#     sleep(1)
#     id = scraper.browser.find_elements(By.XPATH, '//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span')
#     if id: scraper.product_id.append(id[0].text)
#     scraper.browser.execute_script("window.scrollTo(0,0);")
#     js2 = scraper.browser.find_elements(By.XPATH, '//button[@id="product-info-tabs-button--1"][.="Materials & Care"]')
#     if js2: js2[0].click()
#     sleep(1)

# pages = ["https://oldnavy.gap.com/browse/category.do?cid=72091&mlink=5360,1,W_flyout_tops",
# 'https://oldnavy.gap.com/browse/category.do?cid=15292&nav=leftnav:women:shop%20by%20category:dresses%20',
# 'https://oldnavy.gap.com/browse/category.do?cid=1051876&nav=leftnav:women:shop%20by%20category:jumpsuits%20%26%20rompers',
# 'https://oldnavy.gap.com/browse/category.do?cid=1124176&nav=leftnav:women:shop%20by%20category:bottoms',
# ]
# for page in pages:
#     scraper.setURL(page)
#     scraper.getProductLinks('//div[@class="product-card"]/div/div[@class="product-card__image-wrapper"]/a', productCount=75, dynamic=True)
#     scraper.scrape('Old Navy',
#     '//h1[@class="product-title__text"]',
#     '//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span',
#     '//div[@id="product-info-tabs-panel--1"]/ul/li[1]/span',
#     '//div[@class="pdp-pricing"]//h2',
#     3,
#     triggerOldNavyJS
#     )

#Reformation
def trigerHomepage():
    button = scraper.browser.find_elements(By.XPATH, '//button[@data-browse-view-options="4"]')
    if button:
        button[0].click()

def triggerProductJS():
    id = scraper.browser.find_elements(By.XPATH, '//meta[@itemprop="sku"]')
    if id:
        scraper.product_id.append(id[0].get_property('content'))
    else: scraper.product_id.append(" ")
    button = scraper.browser.find_elements(By.XPATH, '//div[@aria-label="Fabric & care"]')
    if button:
        button[0].click()

scraper.setURL('https://www.thereformation.com/categories/shop?types%5B%5D=Bodysuit&types%5B%5D=Jeans&types%5B%5D=Long+Dresses&types%5B%5D=Long+Jumpsuits&types%5B%5D=Midi+Dresses&types%5B%5D=Pants&types%5B%5D=Short+Dresses&types%5B%5D=Shorts&types%5B%5D=Skirts&types%5B%5D=Sweaters&types%5B%5D=Tees')
scraper.getProductLinks('//div[@class="product-grid__cell"]/div/div/a[@class="product-summary__media-link"]', productCount=250, dynamic=True, function=trigerHomepage)
scraper.scrape('Reformation',
'//h1[@class="pdp__name"]',
'//div[@class="doesnotexist"]',
'//ul[@class="pdp-product-data"]/li[contains(., "%")]',
'//p[@class="product-prices__price"]/span',
function=triggerProductJS,
delay=10
)

scraper.processData('output.csv')
scraper.exit()