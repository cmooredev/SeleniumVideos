from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import selenium.webdriver.common.keys
import config
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

port = config.rand_port()
proxy = f'{config.ip}:{port}'
options.add_argument(f'--proxy-server={proxy}')

options.page_load_strategy = 'normal'

driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",)

driver.implicitly_wait(5)
driver.get('https://bot.incolumitas.com/')

#explicit
#challenge = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.ID, 'botChallengeContainer'))

#implicit
challenge = driver.find_element(By.ID, 'botChallengeContainer')

name_field = challenge.find_element(By.NAME, 'userName')
name_field.click()
#remove current content from field
name_field.clear()
name_field.send_keys('cmoorelabs')
time.sleep(10)
driver.quit()
