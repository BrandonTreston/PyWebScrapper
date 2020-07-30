from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from random import randint
from datetime import datetime
import pandas as pd
import re


class Scraper:
    def __init__(self):
        self.options = Options()
        self.options.headless = False
        self.path = 'chromedriver.exe'
        self.browser = webdriver.Chrome(self.path, options=self.options) #pass options as second argument to run browser without gui
        self.headers = {"Accept-Language": "en-US,en;q=0.5"}
        self.url = ''

        #data storage
        self.brand = []
        self.product_name = []
        self.product_description = []
        self.product_id = []
        self.price = []
        self.page_title = []
        self.extraction_time = []
        self.page_url = []
        # product composition storage
        self.cotton = []
        self.leather = []
        self.polyester = []
        self.acrylic = []
        self.rayon = []
        self.modal = []
        self.spandex = []
        self.nylon = []
        self.ployamide = []
        self.viscose = []
        self.elastane = []
        self.linnen = []
        self.lyocell = []
        self.compositionString = []
        self.composition = [self.leather, self.cotton, self.polyester, self.acrylic, self.rayon, self.modal, self.spandex, self.nylon, self.ployamide, self.viscose, self.elastane, self.linnen, self.lyocell]
        #links for each product
        self.links = []

    #load dynamic content by scrolling to bottom of page    
    def getProductLinks(self, productSelector, pages=0, productCount=250, buttonSelector='', function=(), paginated=False, dynamic=False):
        """Gets a list of all web elements containing links to the individual product pages

        Parameters
        ----------
        productSelector : str
            string containing XPATH find product links
        pages : int (optional)
            number of pages containing product links
        productCount : int (optional)
            Number of products to scrape. Defaults to 250. It is reccomended to use this parameter to limit the number of items to be scraped if desired.
        buttonSelector : str (optional)
            Tells the scraper the xpath for the element that will send the scraper to the next page, avoiding complicated URL manipulation for each site.
        function : method (option)
            Executes before data is scraped. Lets user pass a method to the scraper if additional instructions are needed to access
            page data. Ex. lets user use XPATH code and selenium to trigger javascript to render elements with desired data to the DOM.
        paginated : bool (optional)
            Tells the scraper if the catalog is paginated. If true, the scraper will navigate between those pages.
        dynamic : bool (optional)
            if true, tells scraper to scroll to bottom of page to load dynamic content
        """
        elements = [] #temporary storage
        sleep(5) #wait for popups
        if function:
            function() #trigger additional js on a page, like close a popup for example.

        if dynamic == True:
            for i in range(0,5):
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)

        if paginated == True:
            for page in range(0,pages):
                sleep(5) #page load
                #find all product links. returns list, stores at elements.
                _elements = (self.browser.find_elements(By.XPATH, productSelector))
                for element in _elements:
                    href = element.get_property('href')
                    elements.append(href)
                button = self.browser.find_elements(By.XPATH, buttonSelector)[0]
                button.click()
        else:
            _elements = (self.browser.find_elements(By.XPATH, productSelector))
            for element in _elements:
                    href = element.get_property('href')
                    elements.append(href)
        #slice the list if it exceeds productcount
        if len(elements) > productCount:
            elements = elements[:productCount]

        for href in elements:
            #get the href attribute of each web element in elements
            self.links.append(href)
  
    def scrape(self, brandName, nameSelector, idSelector, compositionSelector, priceSelector, delay=5, function=()):
        """Visits each link and scrapes the page using provided XPATH parameters.

        Parameters
        ----------
        brandName : str
            Name of brand from which the article of clothing is from.
        nameSelector : str
            XPATH string for XML/HTML web element containing productg name.
        idSelector: str
            String containing XPATH for the product id web element
        compositionSelector : str
            String containing XPATH for the composition web element
        priceSelector : str
            String containing XPATH for the price web element
        delay : int (optional)
            Sets the delay to scrape each product, as specified in a site's robots.txt file. Defaults to 3 seconds.
        function : method (option)
            Executes before data is scraped. Lets user pass a method to the scraper if additional instructions are needed to access
            page data. Ex. lets user use XPATH code and selenium to trigger javascript to render elements with desired data to the DOM.
        """
        for link in self.links:
            self.browser.get(link)
            sleep(delay)
            if function:
                function()
            #scrape web elements containing desired data: temporary storage
            name = self.browser.find_elements(By.XPATH, nameSelector)
            _id = self.browser.find_elements(By.XPATH, idSelector)
            composition = self.browser.find_elements(By.XPATH, compositionSelector)
            title = self.browser.title
            _price = self.browser.find_elements(By.XPATH, priceSelector)
            tempComp = []

            #determine product type by its name
            getType = self.getType(name[0].text)
            if getType:
            #check if data exists after scraping, add it to data proper store if so

                if link:
                    self.page_url.append(link)
                if brandName:
                    self.brand.append(brandName)
                if name:
                    self.product_name.append(name[0].text)
                if _id:
                    self.product_id.append(_id[0].text)
                if _price:
                    self.price.append(_price[0].text)
                else:
                    self.price.append('n/a')
                if composition:
                    compStr = composition[0].text.lower()
                    self.compositionString.append(compStr)
                    materials = ["leather", "cotton", "polyester", "acrylic", "rayon", "modal", "spandex", "nylon", "polyamide", "viscose", "elastane", "linnen", "lyocell"]
                    for index, material in enumerate(materials):
                        percentage = re.findall( '\d+\D (?=' + material + ')', compStr)
                        if percentage:
                            self.composition[index].append(percentage[0])
                        else:
                        self.composition[index].append('n/a')
                if title:
                    self.page_title.append(title)
                self.extraction_time.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

    def getType(self, productInput):
        """Checks product name for keywords to determine basic article type.

        Parameters
        ----------
        productInput : str
            String containing the product name.
        """
        productName = productInput.lower()
        type = ''
        if 'shirt' in productName or 'top' in productName or 'blouse' in productName or 'tee' in productName or 'cami' in productName:
            type = 'top'
        elif 'hood' in productName or 'jacket' in productName or 'sweatshirt' in productName or 'sweater' in productName or 'cardigan' in productName or 'pullover' in productName:
            type = 'outterwear/jacket'
        elif 'jean' in productName or 'slack' in productName or 'jogger' in productName or 'legging' in productName or 'pant' in productName or 'skirt' in productName or 'short' in productName:
            type = 'bottoms'
        elif 'dress' in productName:
            type = 'dress'
        elif 'romper' in productName or 'bodysuit' in productName or 'jump' in productName or 'suit' in productName or 'coverall' in productName:
            type = 'bodysuit/romper'
        elif 'bra' in productName or 'shoe' in productName or 'bag' in productName or 'bikini' in productName or 'flip' in productName or 'thong' in productName or 'belt' in productName or 'mask' in productName or 'hat' in productName or 'tote' in productName or 'scarf' in productName or 'slides' in productName or 'sock' in productName or 'sneaker' in productName or 'sandal' in productName or 'slip-on' in productName or 'pumps' in productName:
            type = 'ignore'
        else:
            type = 'other'
        if type != 'ignore':
            self.product_description.append(type)
            self.clearLinks()
            return True
        else:
            return False

    def processData(self):
        print(self.brand)
        print(self.product_name)
        print(self.product_id)
        print(self.product_description)
        print(self.extraction_time)
        print(self.page_title)
        print(self.price)
        print(self.compositionString)
        print(self.leather)
        print(self.cotton)        
        print(self.polyester)
        print(self.acrylic)
        print(self.rayon)
        print(self.modal)
        print(self.spandex)
        print(self.nylon)
        print(self.ployamide)
        print(self.viscose)
        print(self.elastane)
        print(self.linnen)
        print(self.lyocell)

        """Create a dataframe for the data agregated by the scrape() method."""
        articles = pd.DataFrame({
            'Brand' : self.brand,
            'Name': self.product_name,
            'Type': self.product_description,
            'ID': self.product_id,
            'Time of Extraction': self.extraction_time,
            'PageTitle': self.page_title,
            'PageUrl': self.page_url,
            'Price': self.price,
            'Composition': self.compositionString,
            'Leather': self.leather,
            'Cotton': self.cotton,
            'Polyester': self.polyester,
            'Acrylic': self.acrylic,
            'Rayon': self.rayon,
            'Modal': self.modal,
            'Spandex': self.spandex,
            'Nylon': self.nylon,
            'Polyamide': self.ployamide,
            'Viscose': self.viscose,
            'Elastane': self.elastane,
            'Linnen': self.linnen,
            'Lyocell': self.lyocell,
        })
        articles.to_csv('output.csv')

    def setURL(self, url):
        """Set the url of the initial catalog page, get it in browser and let load for 4 seconds.

        Parameters
        ----------
        url : str
            the string of the url to navigate to.
        """
        self.url = url
        self.browser.get(url)
        sleep(4)

    def exit(self):
        """Close browser and notify done.
        """
        self.browser.close()
        print('Done.')

    def clearLinks(self):
        """Clear Links list for other pages to use.
        """
        self.links = []

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

# #american apparel
def closeAPPopUp():
    closeButton = scraper.browser.find_elements(By.XPATH, '//img[@aria-label="Popup Close Button"]')[0]
    if closeButton:
        closeButton.click()

scraper.setURL("https://americanapparel.com/women/?_bc_fsnf=1&Product+Type%5B%5D=Bodysuits&Product+Type%5B%5D=Camis&Product+Type%5B%5D=Cardigans&Product+Type%5B%5D=Dresses&Product+Type%5B%5D=Hoodies&Product+Type%5B%5D=Jackets&Product+Type%5B%5D=Jeans&Product+Type%5B%5D=Joggers&Product+Type%5B%5D=Jumpsuits&Product+Type%5B%5D=Leggings&Product+Type%5B%5D=Pants&Product+Type%5B%5D=Shorts&Product+Type%5B%5D=Skirts&Product+Type%5B%5D=Sweaters&Product+Type%5B%5D=Sweatshirts&Product+Type%5B%5D=T-Shirts")
scraper.getProductLinks('//a[@class="plp-product-link"]',0, 250, function=closeAPPopUp, paginated=False, dynamic=True,)
scraper.scrape('American Apparel',
'//h1[@class="productView-title"]',
'//dd[@class="productView-info-value"]',
'//div[@class="product-fabric-details"]//div[2]//div[1]//p[2]',
'//div[@class="price-does-not-exist"]')

#GAP
def closeGapPopUp():
    closePopUpButton = scraper.browser.find_elements(By.XPATH, '//button[@class="css-1qosac6"]')[0]
    if closePopUpButton:
        closePopUpButton.click()
    js_string = "var element = document.getElementById('promoBannerMain');element.remove();"
    scraper.browser.execute_script(js_string)
    offset = scraper.browser.find_element(By.XPATH, '//button[@class="css-1kxwv5e"]')
    scraper.browser.execute_script("arguments[0].scrollIntoView();", offset)
def triggerGapJS():
    js = scraper.browser.find_elements(By.XPATH, '//button[@class="pdp-drawer-trigger"]')[0]
    if js:
        js.click()

scraper.setURL('https://www.gap.com/browse/category.do?cid=1127938#pageId=0&department=136&nav=leftnav:women:categories')
scraper.getProductLinks('//a[@class="product-card__link"]', pages= 5, productCount=250, buttonSelector='//nav[@class="css-1l418ga-Paginator"]/button[@aria-label="Next Page"]', function=closeGapPopUp, paginated=True, dynamic=False)
scraper.scrape('GAP',
'//h1[@class="product-title__text"]',
'//div[@id="product-info-tabs-panel--0"]/ul/li[last()]/span',
'//div[@id="product-info-tabs-panel--1"]/ul/li[1]/span',
'//div[@class="pdp-pricing"]/h2',
3,
triggerGapJS)

scraper.processData()
scraper.exit()