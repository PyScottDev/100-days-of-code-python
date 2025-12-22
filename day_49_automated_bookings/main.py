from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime, date
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException, WebDriverException
import time

RETRY_EXCEPTIONS = (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    WebDriverException,
)

ACCOUNT_EMAIL = "scott@test.com"
ACCOUNT_PASSWORD = "MyPassword"
GYM_URL = "https://appbrewery.github.io/gym/"
TARGET_DAYS = {"tue", "thu"}



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get(GYM_URL)
driver.set_window_size(1400, 900)



# Simple retry wrapper
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except RETRY_EXCEPTIONS as e:
            last_err = e
            if i == retries - 1:
                raise
            time.sleep(1)
    raise last_err

# Function to perform entire login process with retry
def login(driver):
    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
    


def book_class(driver):
    booked = 0
    book_attempts = 0
    waitlists_joined = 0
    already_booked_waitlistd = 0 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='day-group-']"))
    )

    all_days = driver.find_elements(By.CSS_SELECTOR, "div[id^='day-group-']")

    for day in all_days:
        element_id = day.get_attribute("id").lower()
        if any(d in element_id for d in TARGET_DAYS):
            day_name = "tue" if "tue" in element_id else "thu"

            all_times = day.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
            for time in all_times:  
                element_time = time.get_attribute("id")
                parts = element_time.split("-")
                time_name = parts[6]
                if time_name == "1800":
                    correct_class = time
                    book_attempts += 1

                    book_class = correct_class.find_element(By.TAG_NAME, "button")
                    class_status = book_class.text
                    class_id = book_class.get_attribute("id")
                    class_parts = class_id.split("-")
                    class_type = class_parts[2]

                    date_parts = [class_parts[3], class_parts[4], class_parts[5]]
                    date_str = "-".join(date_parts)
                    dt = datetime.strptime(date_str, "%Y-%m-%d")
                    date_final = dt.strftime("%B %d")

                    if class_status == "Booked":
                        print(f"Already booked: {class_type.capitalize()} Class on {day_name.capitalize()}, {date_final}")
                        already_booked_waitlistd += 1
                    elif class_status == "Waitlisted":
                        print(f"Already on waitlist: {class_type.capitalize()} Class on {day_name.capitalize()}, {date_final}")
                        already_booked_waitlistd += 1
                    elif class_status == "Join Waitlist":
                        btn_id = book_class.get_attribute("id")
                        book_class.click()

                        WebDriverWait(driver, 10).until(
                            lambda d: d.find_element(By.ID, btn_id).text in ("Waitlisted", "Booked")
                        )

                        print(f"Joined waitlist for: {class_type.capitalize()} Class on {day_name.capitalize()}, {date_final}")
                        waitlists_joined += 1
                    elif class_status == "Book Class":
                        btn_id = book_class.get_attribute("id")
                        book_class.click()

                        WebDriverWait(driver, 10).until(
                            lambda d: d.find_element(By.ID, btn_id).text in ("Booked", "Waitlisted")
                        )

                        print(f"Successfully booked: {class_type.capitalize()} Class on {day_name.capitalize()}, {date_final}")
                        booked += 1

    return booked, waitlists_joined, already_booked_waitlistd,book_attempts


def get_my_bookings(driver):
    booked_counter = 0
    my_bookings = driver.find_element(By.ID, "my-bookings-link")
    my_bookings.click()

    when_ps = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//p[strong[normalize-space()='When:']]"))
    )

    for n in when_ps:
        try:
            booked_parts = n.text.split()
            booked_day = booked_parts[1].lower().strip(",")
            if booked_day in TARGET_DAYS:
                booked_counter +=1
        except NoSuchElementException:
            pass
    return booked_counter


#print(booked_counter, booked)

retry(lambda: login(driver), description="login")
booked, waitlists_joined, already_booked_waitlistd, book_attempts = retry(lambda: book_class(driver), description="book class")
booked_counter = retry(lambda: get_my_bookings(driver), description="get_my_bookings")

# --- SIMPLE SUMMARY + VERIFICATION OUTPUT ---

expected = book_attempts  # how many Tue/Thu 6pm classes you processed
found = booked_counter    # how many Tue/Thu bookings appear on My Bookings page

print("\n--- BOOKING RUN SUMMARY ---")
print(f"Processed Tue/Thu 6pm classes: {expected}")
print(f"Booked this run: {booked}")
print(f"Waitlists joined this run: {waitlists_joined}")
print(f"Already booked/waitlisted: {already_booked_waitlistd}")

print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
print(f"Found Tue/Thu bookings on My Bookings page: {found}")

print("\n--- VERIFICATION RESULT ---")
print(f"Expected (processed): {expected}")
print(f"Found (on My Bookings): {found}")

if found >= expected:
    print("✅ OK: Verification looks ok (found >= processed).")
else:
    print("❌ MISMATCH: Found fewer bookings than processed.")


#print("--- BOOKING SUMMARY ---")
#print(f"Classes booked: {booked}\nWaitlists joined: {waitlists_joined}\nAlready booked/waitlisted: {already_booked_waitlistd}")


