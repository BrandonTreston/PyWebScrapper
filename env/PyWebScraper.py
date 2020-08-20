from time import sleep
from datetime import datetime
import pandas as pd
import re

from selenium import webdriver
from selenium.webdriver.common.by import By

class Scraper:
    def __init__(self):
        self.path = 'chromedriver.exe'
        self.browser = webdriver.Chrome(self.path)
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
        #product composition storage
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
        self.linen = []
        self.lyocell = []
        self.compositionString = []
        self.composition = [self.leather, self.cotton, self.polyester, self.acrylic, self.rayon, self.modal, self.spandex, self.nylon, self.ployamide, self.viscose, self.elastane, self.linen, self.lyocell]
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
        sleep(3) #wait for popups
        if function:
            function() #trigger additional js on a page, like close a popup for example.

        #scroll to load dynamic content (does not work on every site. One example is GAP)
        if dynamic == True:
            i = 0
            while i < 7000:
                self.browser.execute_script("window.scrollBy(0,10);") #scroll by 10px
                i += 1
            self.browser.execute_script("window.scrollTo(0,0);") #scroll to top
            sleep(4)

        if paginated == True:
            for page in range(0,pages):
                sleep(3) #page load
                #find all product links. returns list, stores at elements.
                _elements = (self.browser.find_elements(By.XPATH, productSelector))
                for element in _elements:
                    href = element.get_property('href')
                    elements.append(href)
                #click next page button
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
        
        #get the href attribute of each web element in elements, add to datastore
        for href in elements:
            self.links.append(href)
  
    def scrape(self, brandName, nameSelector, idSelector, compositionSelector, priceSelector, delay=5, function=(), doName= True, doId= True, doComposition= True, doPrice= True):
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
        doName : bool (optional)
            tells the scraper to not scrape for product name in the event that the name is obscured on the page and must be handeled by a secondary function. Default is True
        doId : bool (optional)
            tells the scraper to not scrape for product id in the event that the id is obscured on the page and must be handeled by a secondary function. Default is True
        doComposition : bool (optional)
            tells the scraper to not scrape for product composition in the event that the composition is obscured on the page and must be handeled by a secondary function. Default is True
        doPrice : bool (optional)
            tells the scraper to not scrape for product price in the event that the price is obscured on the page and must be handeled by a secondary function. Default is True
        """
        for link in self.links:
            self.browser.get(link)
            sleep(delay)
            materials = ["leather", "cotton", "polyester", "acrylic", "rayon", "modal", "spandex", "nylon", "polyamide", "viscose", "elastane", "linen", "lyocell"]
            
            if function:
                function() #trigger additional JS, like click a menu button to make content appear
            #scrape web elements containing desired data: temporary storage
            name = self.browser.find_elements(By.XPATH, nameSelector)
            _id = self.browser.find_elements(By.XPATH, idSelector)
            composition = self.browser.find_elements(By.XPATH, compositionSelector)
            title = self.browser.title
            _price = self.browser.find_elements(By.XPATH, priceSelector)

            #check if data exists after scraping, add it to data proper store if so
            if link: self.page_url.append(link)
            if brandName:self.brand.append(brandName)
            if doName:
                if name:
                    self.product_name.append(name[0].text)
                    #determine product type by its name
                    self.getType(name[0].text)
                else:
                    self.product_name.append(' ')
                    self.product_description.append(' ')
            if doId:
                if _id:
                    self.product_id.append(_id[0].text)
                else: self.product_id.append(' ')
            if doPrice:
                if _price:
                    self.price.append(_price[0].text)
                else: self.price.append(' ')
            if doComposition:
                if composition:
                    compStr = ''
                    for index, item in enumerate(composition):
                        compStr += composition[index].text.lower()
                    self.compositionString.append(compStr)
                    self.sort(compStr)
                else:
                    self.compositionString.append(' ')
                    for index, material in enumerate(materials):
                        self.composition[index].append(' ')
            if title: self.page_title.append(title)
            else: self.page_title.append(" ")
            self.extraction_time.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

    def sort(self, compStr):
        """Sorts the composition string for each product into columns.

        Parameters
        ----------
        compStr : str
            The string containting the text content of a produt's composition
        """
        #for each item in materials, RegEx find '% + material name' and 'material name + %' then add to datastore. Order of the composition[] datastore MUST coincide with the order of the materials[] list.
        materials = ["leather", "cotton", "polyester", "acrylic", "rayon", "modal", "spandex", "nylon", "polyamide", "viscose", "elastane", "linen", "lyocell"]
        for index, material in enumerate(materials):
                        percentage = re.findall( '\d+\D (?=' + material + ')', compStr)
                        percentage2= re.findall('(?<=' + material + ') \d+\D', compStr)
                        if percentage:
                            self.composition[index].append(percentage[0])
                        elif percentage2:
                            self.composition[index].append(percentage2[0].strip())
                        else:
                            self.composition[index].append(' ')

    def getType(self, productInput):
        """Checks product name for keywords to determine basic article type.

        Parameters
        ----------
        productInput : str
            String containing the product name.
        """
        if productInput:
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
            elif 'bra' in productName or 'shoe' in productName or 'boot' in productName or 'bag' in productName or 'bikini' in productName or 'flip' in productName or 'thong' in productName or 'belt' in productName or 'mask' in productName or 'hat' in productName or 'tote' in productName or 'scarf' in productName or 'slides' in productName or 'sock' in productName or 'sneaker' in productName or 'sandal' in productName or 'slip-on' in productName or 'pumps' in productName:
                type = 'ignore'
            else:
                type = 'other'
            self.product_description.append(type)
            self.clearLinks()

    def processData(self, filename):
        # For Debug
        print(len(self.brand))
        print(len(self.product_name))
        print(len(self.product_id))
        print(len(self.product_description))
        print(len(self.price))
        print(len(self.extraction_time))
        print(len(self.page_title))
        print(len(self.compositionString))
        print(len(self.leather))
        print(len(self.cotton))
        print(len(self.polyester))
        print(len(self.acrylic))
        print(len(self.rayon))
        print(len(self.modal))
        print(len(self.spandex))
        print(len(self.nylon))
        print(len(self.ployamide))
        print(len(self.viscose))
        print(len(self.elastane))
        print(len(self.linen))
        print(len(self.lyocell))

        """Create a dataframe for the data agregated by the scrape() method.
        
        parameters
        ----------
        filename : str
            Name of the file to which the scraper will output.
        """
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
            'linen': self.linen,
            'Lyocell': self.lyocell,
        })
        articles.to_csv(filename)

    def setURL(self, url):
        """Set the url of the initial catalog page, get it in browser and let load for 4 seconds.

        Parameters
        ----------
        url : str
            the string of the url to navigate to.
        """
        self.browser.maximize_window()
        self.url = url
        self.browser.get(url)
        sleep(1)

    def exit(self):
        """Close browser and notify done.
        """
        self.browser.close()
        print('Done.')

    def clearLinks(self):
        """Clear Links list for other pages to use.
        """
        self.links = []
