from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        ####Stealth options#####
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        ####Stealth options#####
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def slow_type(self, element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(random.uniform(0.1, 0.3)) # Human-like typing speed

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        try:
            cookies_reject = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))
                )
            cookies_reject.click()
        except:
            pass  # cookies not shown

        start_test = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start_test.click()

        time.sleep(80)
        download_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload_speed = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        #self.driver.quit()
        return download_speed, upload_speed


    def tweet_at_provider(self, email, username, password, promised, download):
        self.driver.get("https://x.com/")
        cookies = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div'))
        )
        cookies.click()
        sign_in_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div"))
        )
        sign_in_button.click()
        username_enter = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']"))
            )
        
        self.slow_type(username_enter, email)
        #username_enter.send_keys(email)
        # text_box = WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][contenteditable='true']"))
        #     )
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        next_button.click()
        # username2 = WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]'))
        #     )
        # username2.send_keys(username)
        # Use the 'name' attribute - it's the gold standard for X login
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "text"))
        )

        self.slow_type(username_field, username)
        #username_field.send_keys(username)
        next_button2 = self.driver.find_element(By.CSS_SELECTOR,"button[role='button']")
        next_button2.click()

        password_enter = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='current-password']"))
            )
        
        self.slow_type(password_enter, password)
        #password_enter.send_keys(password)
        log_in_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
        log_in_box.click()
        

        text_box = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][contenteditable='true']"))
            )
        text_box.send_keys(f"Ah ah! So you promised {promised}Mbps and I only get {download}Mbps")
        post_button = self.driver.find_element(By.CSS_SELECTOR, "button[role='button']")
        post_button.click()
        
