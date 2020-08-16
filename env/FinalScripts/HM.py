from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# H&M
scraper.setURL('https://www2.hm.com/en_us/women/products/view-all.html?sort=stock&productTypes=Blazer,Blouse,Body,Cardigan,Coat,Dress,Jacket,Jeans,Jumper,Jumpsuit,Leggings,Pants,Shirt,Shorts,Skirt,T-shirt,Top&image-size=small&image=model&offset=0&page-size=250')
scraper.getProductLinks('//h3[@class="item-heading"]//a[@class="link"]', pages=0, productCount=250)
scraper.scrape('H&M',
'//h1[@class="primary product-item-headline"]',
'//dl[@class="pdp-description-list"]/div/dt[text()="Art. No."]//following-sibling::dd',
'//dl[@class="pdp-description-list"]/div/dt[text()="Composition"]//following-sibling::dd',
'//span[@class="price-value"]'
)

scraper.processData('OutputHM.csv')
scraper.exit()