from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

#JCPenny
pages = ['https://www.jcpenney.com/g/women/womens-tops?id=cat100210006&cm_re=ZI-_-DEPARTMENT-_-VN-_-DEPT-WOMENS-X2-1-_-TOPS-_-DESKTOP_1',
'https://www.jcpenney.com/g/women/womens-dresses?id=cat100210008&boostIds=ppr5007944251&cm_re=ZI-_-DEPARTMENT-_-VN-_-DEPT-WOMENS-_-VN-2-_-DRESSES-_-DESKTOP_2',
'https://www.jcpenney.com/g/women/womens-pants?id=cat100250095&cm_re=ZI-_-DEPARTMENT-_-VN-_-DEPT-WOMENS-_-VN-3-_-PANTS-_-DESKTOP_3',
'https://www.jcpenney.com/g/women/womens-shorts?id=cat100250098&cm_re=ZI-_-DEPARTMENT-_-VN-_-DEPT-WOMENS-X2-5-_-SHORTS-_-DESKTOP_5',
'https://www.jcpenney.com/g/women/womens-jeans?id=cat100250096&cm_re=ZI-_-DEPARTMENT-_-VN-_-DEPT-WOMENS-X2-7-_-JEANS-_-DESKTOP_7',
'https://www.jcpenney.com/g/women/womens-skirts?id=cat100250097&cm_re=ZI-_-DEPARTMENT-_-VN-_-DEPT-WOMENS-X2-8-_-SKIRTS-_-DESKTOP_8']
for page in pages:
    scraper.setURL(page)
    scraper.getProductLinks('//a[@class="_3Duud"]', productCount=45)
scraper.scrape('JCPenny',
'//h1[@aria-label="productTitle"]',
'//span[@class="_3_di8"]',
'//li[contains(.,"Fabric Content")]',
'//p[@class="_3kQtR"]/span/span')

scraper.processData('OutputJCPenny.csv')
scraper.exit()