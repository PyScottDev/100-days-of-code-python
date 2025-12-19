from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.set_window_size(1400, 900)

print("Loaded page:", driver.title) #debugging


#article_count = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")

#print(article_count[1].text)
#article_count[1].click()

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
#driver.quit()

