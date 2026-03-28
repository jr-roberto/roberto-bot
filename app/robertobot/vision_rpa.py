import os
import pyautogui
from PIL import Image
from io import BytesIO
from pyautogui import Point

from app.drivers.chrome import Chrome, ActionChains

class FindImage:
    def __init__(self, point:Point , rect:dict, driver):
        self.point  = point
        self.rect   = rect
        self.driver = driver
    
    def click(self):
        action = ActionChains(driver=self.driver)

        try:
            action.move_by_offset(self.point.x , self.point.y)
            action.click()
            action.perform()
            action.reset_actions()

        except:
            raise ValueError(f"Erro ao realizar click nas coordenadas {self.point.x}, {self.point.y} -> {self.driver.get_window_rect()}")

    def click_relative(self, x:int, y:int):
        self.point.x = self.point.x + x
        self.point.y = self.point.y + y
        self.click()

class VisionRpa:
    def __init__(self):
        super().__init__()
        self.driver:Chrome
        self.cutouts_path = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__))), "cutouts")

    def find_image(self, value:str):
        cutout_file = os.path.join(self.cutouts_path, f"{value}.png")
        
        # captura o screenshot como bytes (PNG em memória)
        png_bytes = self.driver.get_screenshot_as_png()

        self.page   = Image.open(BytesIO(png_bytes))
        self.cutout = Image.open(cutout_file)

        box     = pyautogui.locate(self.cutout, self.page)
        point   = pyautogui.center(box)
        rect    = {'height': int(box.height), 'width': int(box.width), 'x': int(box.left), 'y': int(box.top)}

        return FindImage(
            point,
            rect,
            self.driver
        )
