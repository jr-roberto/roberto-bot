from app.drivers.chrome import ChromeDriver
from selenium.webdriver.common.by import By

class Bot(ChromeDriver):
    def __init__(self, url:str = "https://google.com"):
        super().__init__()
        self.driver.get(url)
    
    
