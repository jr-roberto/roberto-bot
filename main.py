from app.bots.google_fotos import Bot
import time

bot = Bot()

bot.localizar_img_google("google")

bot.pesquisar("Automacao RPA")

time.sleep(10)

bot.driver.quit()
