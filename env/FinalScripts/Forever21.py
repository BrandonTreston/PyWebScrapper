from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# Forever21
def closeF21Popup():
    sleep(11) #wait for popup
    button = scraper.browser.find_elements(By.XPATH, '//button[@aria-label="Decline Offer; close the dialog"]')
    if button:
        button[0].click()

scraper.setURL('https://www.forever21.com/us/shop/catalog/category/f21/app-main')
scraper.getProductLinks('//a[@class="item_slider product_link"]', buttonSelector='//span[@class="p_next"]', paginated=True, productCount=250, pages=5, function=closeF21Popup )
scraper.scrape('Forever 21',
'//h1[@id="h1Title"]',
'//div[@id="tabDescriptionContent"]/span[@class="t_mid pt_10"]',
'//div[@id="divDescription"]/section[2]/div/p[contains(., "%")]',
'//div[@id="ItemPrice"]/div/span')

scraper.processData('OutputF21.csv')
scraper.exit()