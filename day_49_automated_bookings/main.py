from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime, date, timedelta

ACCOUNT_EMAIL = "scott@test.com"
ACCOUNT_PASSWORD = "MyPassword"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)
driver.set_window_size(1400, 900)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

email_enter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email-input"))
)
email_enter.send_keys(ACCOUNT_EMAIL)

password_enter = driver.find_element(By.ID, "password-input")
password_enter.send_keys(ACCOUNT_PASSWORD)

submit_button = driver.find_element(By.ID, "submit-button")
submit_button.send_keys(Keys.ENTER)

# today = datetime.now()
# print(today)
# booking_date = today.replace(hour=18, minute=0, second=0, microsecond=0) + timedelta(days=6)
# print(booking_date)
#book-button-spin-2025-12-22-1800


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p[id^='class-time-']"))
)
classes = driver.find_elements(By.CSS_SELECTOR, "p[id^='class-time-']")
for n in classes:
    print(n.get_attribute("id"))