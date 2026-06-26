"""Home page object"""
from pages.base_page import BasePage
from data.locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    
    def click_signup_login(self):
        self.click_element(HomePageLocators.SIGNUP_LOGIN_LINK)
    
    def click_products(self):
        self.click_element(HomePageLocators.PRODUCTS_LINK)
    
    def click_cart(self):
        self.click_element(HomePageLocators.CART_LINK)
    
    def click_logout(self):
        self.click_element(HomePageLocators.LOGOUT_LINK)
    
    def is_logout_visible(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located(HomePageLocators.LOGOUT_LINK))
            return True
        except:
            return False