import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

addresses_el = soup.find_all("address")

property_records = []

property_el = soup.find_all("article", attrs={"data-test": "property-card"})
for property in property_el:
    address = property.find("address").get_text(strip=True)
    price_dirty = property.find("span", attrs={"data-test": "property-card-price"}).get_text(strip=True)
    link = property.find("a").get("href")
    
    digits_only = "".join([char for char in price_dirty if char.isdigit()])
    price = f"${digits_only[:1]},{digits_only[1:4]}"
    property_card = {
        "address": address,
        "price": price,
        "link": link,
        }
    property_records.append(property_card)
    print(price)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get("https://forms.gle/PDjKUyPmcyfCezYC8")


for record in property_records: 
    address_input = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input.whsOnd.zHQkBf[aria-labelledby~="i1"]')
        )
    )
    address_input.send_keys(record["address"])

    price_input = driver.find_element(
        By.CSS_SELECTOR,
        'input.whsOnd.zHQkBf[aria-labelledby~="i6"]'
    )
    price_input.send_keys(record["price"])

    link_input = driver.find_element(
        By.CSS_SELECTOR,
        'input.whsOnd.zHQkBf[aria-labelledby~="i11"]'
    )
    link_input.send_keys(record["link"])

    submit = driver.find_element(By.CSS_SELECTOR, ".NPEfkd.RveJvd.snByac")
    submit.click()

    submit_another = driver.find_element(By.CSS_SELECTOR, "a")
    submit_another.click()


