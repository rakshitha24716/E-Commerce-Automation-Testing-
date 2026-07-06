import os
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")

    if os.environ.get("CI"):
        chrome_options.add_argument("--headless=new")

    prefs = {
        "profile.default_content_setting_values.ads": 2,
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(120)

    yield driver
    driver.quit()
