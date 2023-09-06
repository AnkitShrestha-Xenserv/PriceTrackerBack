from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from models.product import Product

DRIVER_PATH = ".\chromedrive\chromedrive.exe"

class Scrap(webdriver.Chrome):
    
    def __init__(self, driver_path=DRIVER_PATH,teardown=False):
        self.teardown = teardown
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_experimental_option("detach", True)
        self.service = Service(executable_path=driver_path)

        super(Scrap,self).__init__(options=self.options,service=self.service)
        self.implicitly_wait(15)
        self.maximize_window()

    # Default exit function
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # Loads the specified URL for scraping
    def loadWebsite(self,url):
        self.get(url)
        
    # Get the details of a specific product from the given URL
    def getProductDetails(self,url):
        self.loadWebsite(url)
        name = self.find_element(by=By.CSS_SELECTOR, value='span[class="pdp-mod-product-badge-title"]').get_attribute('innerHTML').strip()
        price = self.find_element(by=By.CSS_SELECTOR, value ='span[class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]').get_attribute('innerHTML').strip()
        #rating = self.find_element(by=By.CSS_SELECTOR, value='span[class="score-average"]').get_attribute('innerHTML').strip()
        return Product(productName = name,currentPrice = price,url = url)
    
    # Experimental Features
        
    # Experimental feature to search for a specific item from the website
    def search(self, item):
        search_element = self.find_element(by=By.CSS_SELECTOR, value = 'input[id="q"]')
        search_element.clear()
        search_element.send_keys(item)
        search_button = self.find_element(by=By.CSS_SELECTOR, value ='button[class="search-box__button--1oH7"]')
        search_button.click()
    
    # Experimental feature to get the top search results of a specific item
    def getTopSearchResults(self):
        data = []
        results = self.find_elements(by=By.CSS_SELECTOR, value ='div[class="box--pRqdD"]')
        for elem in results:
            name = elem.find_element(by=By.CSS_SELECTOR, value ='div[class="title--wFj93"]').find_element(by=By.TAG_NAME,value = 'a').get_attribute('innerHTML').strip()
            price = elem.find_element(by=By.CSS_SELECTOR, value='span[class="currency--GVKjl"]').get_attribute('innerHTML').strip()
            data.append(Product(name,price))
        
        return data
    
    
        
        
        