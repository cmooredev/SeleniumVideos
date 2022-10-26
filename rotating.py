from selenium import webdriver
from selenium.webdriver.common.by import By
from time
import random
import config

def rand_port():
    port = random.choice(config.ips)
    return port

def main():
    #chrome options for setting the proxy
    chrome_options = webdriver.ChromeOptions()
    #add argument with proxy infos
    proxy = rand_proxy()
    chrome_options.add_argument(f'--proxy-server={config.ip}:{port}')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://myexternalip.com/raw')
    print(proxy)
    sleep(2)
    driver.quit()

main()
