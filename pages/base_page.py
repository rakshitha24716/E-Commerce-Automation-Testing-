"""Base page class for all page objects"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def close_ad_if_present(self):
        try:
            self.driver.switch_to.default_content()
            frames = self.driver.find_elements(By.TAG_NAME, "iframe")
            for frame in frames:
                try:
                    self.driver.execute_script("arguments[0].remove();", frame)
                except:
                    pass
        except:
            pass

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        self.close_ad_if_present()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.close_ad_if_present()
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", element)
    
    def send_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def take_screenshot(self, name):
        self.driver.save_screenshot(f"screenshots/{name}.png")
    
    def go_to_url(self, url):
        self.driver.get(url)
        time.sleep(2)
        self.close_ad_if_present()
    
    def get_current_url(self):
        return self.driver.current_url