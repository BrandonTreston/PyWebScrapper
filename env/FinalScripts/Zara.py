from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# zara
def getComposition():
    closeChat = scraper.browser.find_elements(By.XPATH, '//button[@class="chat-close"]')
    if closeChat:
        closeChat[0].click()
    button = scraper.browser.find_elements(By.XPATH, '//a[@class="_product-composition"]')
    if button:
        button[0].click()
        sleep(3)
    compStrings = []
    we = scraper.browser.find_elements(By.XPATH, '//ul[@class="list-composition"]/li/p')
    for index, element in enumerate(we):
        compStrings.append(we[index].text)
    newlinestring = ''.join(compStrings)
    finalString = newlinestring.replace('\n', ' ')
    scraper.compositionString.append(finalString)

pages = ['https://www.zara.com/us/en/woman-tshirts-l1362.html?v1=1549244',
'https://www.zara.com/us/en/woman-body-l1057.html?v1=1549303',
'https://www.zara.com/us/en/woman-trousers-l1335.html?v1=1549251',
'https://www.zara.com/us/en/woman-jeans-l1119.html?v1=1549248',
'https://www.zara.com/us/en/woman-trousers-shorts-l1355.html?v1=1549447',
'https://www.zara.com/us/en/woman-skirts-l1299.html?v1=1549246']
for page in pages:
    scraper.setURL(page)
    scraper.getProductLinks('//a[@class="item _item"]', productCount=50)
scraper.scrape('Zara',
'//h1[@class="product-name"]',
'//span[@data-qa-qualifier="product-reference"]',
'//ul[@class="handeled-by-function"]',
'//div[@class="price _product-price"]/span',
function=getComposition,
doComposition=False)

scraper.processData('OutputZara.csv')
scraper.exit()