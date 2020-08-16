from PyWebScraper import Scraper 
from selenium.webdriver.common.by import By
from time import sleep
scraper = Scraper()

# #urban outfitters THEY DONT PERMIT ACCESS TO THE SITE USING AUTOMATION TOOLS AT ALL EVEN WHEN FOLLOWING THEIR ROBOTS.TXT RULES. 
# # THEY WILL BAN YOUR IP ADDRESS FOR USING THIS SCRIPT EXERCISE EXTREME CAUTION AND USE A VPN. THIS IS IMPORTANT BECAUSE MANY OF
# # THESE SITES SHARE THE SAME BLACKLIST, SO GETTING BANNED FROM ONE RESULTS IN BANS FROM MANY OF THE SITES HERE.

# # pages = ['https://www.urbanoutfitters.com/dresses',
# # 'https://www.urbanoutfitters.com/womens-tops',
# # 'https://www.urbanoutfitters.com/womens-denim',
# # 'https://www.urbanoutfitters.com/womens-bottoms',
# # ]
# # scraper.setURL(pages[0])
# # sleep(3)
# # scraper.browser.refresh() #
# # for page in pages:
# #     scraper.setURL(page)
# #     scraper.getProductLinks('//div[@class="c-pwa-product-tile"]/a', productCount=70, dynamic=True)
# # scraper.scrape('Urban Outfitters',
# # '//h1[@class="c-pwa-product-meta-heading"]',
# # '//div[@class="o-pwa-content-group"]/p/span[contains(.,";")]',
# # '//div[@class="s-pwa-cms c-pwa-product-details"]/div/div/p[contains(.,"%")]',
# # '//p[@class="c-pwa-product-price"]/span',
# # delay=10)

scraper.processData('OutputUrbanOutfitters.csv')
scraper.exit()