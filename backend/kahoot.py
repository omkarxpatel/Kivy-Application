import time
from kivymd.toast import toast

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

def kahoot():
    service = Service(executable_path='/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get("https://kahootbot.org")

    # toast("Fetching Browser...")

    try:
        pinXpath = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content-wrap"]/div[1]/div[2]/div[1]/div/input')))
        nickXpath = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content-wrap"]/div[1]/div[2]/div[2]/div/input')))
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content-wrap"]/div[1]/div[2]/div[3]/button')))
        
        # toast("Fetching xPaths...")
        
    except NoSuchElementException:
        # toast("Error: Element not found.")
        driver.quit()
        return

    try:
        nickXpath.send_keys("name")
        pinXpath.send_keys("550782")
        driver.execute_script("arguments[0].click();", button)  

        
        # toast("Sending Bots...")
        
    except ElementNotInteractableException:
        # toast("Error: Button not interactable.")
        driver.quit()
        return

    try:
        time.sleep(100)
    finally:
        driver.quit()


kahoot()
