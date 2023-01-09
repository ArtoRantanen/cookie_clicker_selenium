from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
website = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(website)
time.sleep(15)

while True:
    for i in range(100):
        driver.find_element(By.ID, 'bigCookie').click()
    try:
        driver.find_element(By.ID, 'upgrade0').click()
    except:
        pass
    try:
        for i in range(19):
            try:
                element = f'product{str(18-i)}'
                driver.find_element(By.ID, element).click()
            except:
                pass
    except:
        pass