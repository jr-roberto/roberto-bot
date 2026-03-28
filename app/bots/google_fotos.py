from app.drivers.chrome import ChromeDriver
from app.robertobot.vision_rpa import VisionRpa

class Bot(ChromeDriver, VisionRpa):
    def __init__(self, url:str = "https://google.com/"):
        super().__init__()
        self.driver.get(url)

    def pesquisar(self, value:str):
        self.to_type(value)
        pass

    def localizar_img_google(self, value:str):
        if self.find_element_image(value=value):
            self.click()
            self.click_relative(0 ,97)
