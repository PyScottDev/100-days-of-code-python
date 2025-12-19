from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
driver.set_window_size(1400, 900)

#languge =  driver.find_element(By.ID, value="langSelect-EN")
language = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)
language.click()

def get_int(text):
    text = text.strip().replace(",", "")
    return int(text)

def cookie_count(driver):
    cookie_text = driver.find_element(By.ID, "cookies").text
    parts = cookie_text.split()
    if not parts:
        return 0.0
    
    number = float(parts[0].replace(",", ""))

    if len(parts) > 1:
        word = parts[1].lower()
        if word.startswith("million"):
            number *= 1_000_000
        elif word.startswith("billion"):
            number *= 1_000_000_000
        elif word.startswith("trillion"):
            number *= 1_000_000_000_000
    return number



def check_upgrades(driver):
    cookies = cookie_count(driver)
    for n in range(19, -1, -1):
        try: 
            price_element = driver.find_element(By.ID, f"productPrice{n}")
            price_text = price_element.text.strip()
            if not price_text:
                continue

            price = get_int(price_text)

            if cookies >= price:   
                driver.find_element(By.ID, f"product{n}").click()
                break

        except (ValueError, IndexError):
            continue

cookie = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)


start_time = time.time()
last_upgrade_check = time.time()

while True:
    current_time = time.time()
    cookie.click()
    if current_time - last_upgrade_check >= 5:
        check_upgrades(driver)
        last_upgrade_check = current_time
