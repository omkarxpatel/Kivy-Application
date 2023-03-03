import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

def kahoot(game_pin, bot_names, root):
    service = Service(executable_path='/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get("https://kahootbot.org")

    print("Fetching Browser...")

    try:
        pinXpath = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content-wrap"]/div[1]/div[2]/div[1]/div/input')))
        nickXpath = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content-wrap"]/div[1]/div[2]/div[2]/div/input')))
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content-wrap"]/div[1]/div[2]/div[3]/button')))
        
        print("Fetching xPaths...")
        
    except NoSuchElementException:
        print("Error: Element not found")
        driver.quit()
        return

    try:
        nickXpath.send_keys(bot_names)
        pinXpath.send_keys(game_pin)
        driver.execute_script("arguments[0].click();", button)  

        
        print("Sending Bots...")
        
    except ElementNotInteractableException:
        print("Error: Button not interactable")
        driver.quit()
        return

    try:
        time.sleep(6000)
    finally:
        driver.quit()