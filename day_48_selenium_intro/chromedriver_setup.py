# chromedriver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver(detach=True):
    """
    Returns a Selenium Chrome driver that works on Chromebook Linux.
    """
    options = Options()
    options.binary_location = "/usr/bin/chromium"   # Use Chromium instead of Chrome

    # Keep browser open after script finishes (like Angela does)
    if detach:
        options.add_experimental_option("detach", True)

    # Path to chromedriver installed via apt
    service = Service("/usr/bin/chromedriver")

    return webdriver.Chrome(service=service, options=options)
