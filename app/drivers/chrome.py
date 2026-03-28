from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from app.robertobot.vision_rpa import VisionRpa, FindImage

class ChromeDriver:
    def __init__(self):
        super().__init__()
        # self.find_image: VisionRpa.find_image

        service = Service(
            executable_path=None
        )
        
        prefs = {
            "intl.accept_languages": "pt-BR,pt",
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "download.extensions_to_open": "",
            "profile.default_content_settings.popups": 0,
            "safebrowsing.enabled": True,
        }

        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--start-maximized")
        options.add_argument("--lang=pt-BR")

        self.driver = Chrome(
            service=service,
            options=options,
        )

        self.set_implicitly_wait(10)

    def set_implicitly_wait(self, value:float):
        self.implicitly_wait:float = value
        self.driver.implicitly_wait(self.implicitly_wait)

    def click(self, xoffset:int = None, yoffset:int = None):
        action = ActionChains(driver=self.driver)

        if xoffset and yoffset: x, y = xoffset, yoffset
        else: x, y = self.last_element_found.point.x ,self.last_element_found.point.y
            
        try:
            action.move_by_offset(x, y)
            action.click()
            action.perform()
            action.reset_actions()
            
        except:
            action.reset_actions()
            raise ValueError(f"Erro ao realizar click nas coordenadas ({x}, {y}) -> {self.driver.get_window_rect()}")
            
    def click_relative(self, x:int, y:int):
        x = self.last_element_found.point.x + x
        y = self.last_element_found.point.y + y
        self.click(x, y)

    def click_context(self):
        action = ActionChains(driver=self.driver)

        try:
            action.move_by_offset(self.last_element_found.point.x, self.last_element_found.point.y)
            action.context_click()
            action.perform()
            action.reset_actions()

        except:
            raise ValueError(f"Erro ao realizar click nas coordenadas ({self.last_element_found.point.x}, {self.last_element_found.point.y}) -> {self.driver.get_window_rect()}")

    def find_element_css_selector(self, value:str):
        self.last_element_found = self.driver.find_element(By.CSS_SELECTOR, value)
        return self.last_element_found

    def find_element_xpath(self, value:str):
        self.last_element_found = self.driver.find_element(By.XPATH, value)
        return self.last_element_found

    def find_element_image(self, value:str):
        "Usando ferramento Roberto Bot -> VisionRpa"
        self.last_element_found = VisionRpa.find_image(self, value)
        return self.last_element_found

    def to_type(self, value:str):
        action = ActionChains(driver=self.driver)

        try:   
            action.send_keys(value)
            action.perform()
            action.reset_actions()

        except:
            action.reset_actions()
            raise ValueError(f"Erro ao tentar digitar '{value}' nas coordenadas ({self.last_element_found.point.x}, {self.last_element_found.point.y}).")

    def enter(self):
        action = ActionChains(driver=self.driver)

        try:   
            action.send_keys(Keys.ENTER)
            action.perform()
            action.reset_actions()

        except:
            action.reset_actions()
            raise ValueError(f"Erro ao tentar digitar 'Keys.ENTER' nas coordenadas ({self.last_element_found.point.x}, {self.last_element_found.point.y}).")

    def tab(self):
        action = ActionChains(driver=self.driver)

        try:   
            action.send_keys(Keys.TAB)
            action.perform()
            action.reset_actions()

        except:
            action.reset_actions()
            raise ValueError(f"Erro ao tentar digitar 'Keys.TAB' nas coordenadas ({self.last_element_found.point.x}, {self.last_element_found.point.y}).")
