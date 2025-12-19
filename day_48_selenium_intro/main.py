from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

# print(f"The price is {price_dollar.text}{price_cents.text}")

# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# link = driver.find_element(By.CSS_SELECTOR, value="documentation-widget a")
# print(link.text)

# upcoming = driver.find_elements(By.CSS_SELECTOR, value=".menu li")
# print(upcoming.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for time in event_times:
    print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for name in event_names:
    print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
    "time": event_times[n].text,
    "name": event_names[n].text,
    }

events2 = {}

print(events)





driver.quit()

