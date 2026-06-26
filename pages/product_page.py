"""Products page object"""
from pages.base_page import BasePage
from data.locators import ProductsPageLocators
from selenium.common.exceptions import StaleElementReferenceException
import time

class ProductsPage(BasePage):
    
    def is_products_title_visible(self):
        try:
            self.driver.find_element("xpath", "//h2")
            return True
        except:
            return False
    
    def search_product(self, product_name):
        self.send_text(ProductsPageLocators.SEARCH_INPUT, product_name)
        self.click_element(ProductsPageLocators.SEARCH_BUTTON)
    
    def get_product_count(self):
        products = self.driver.find_elements(*ProductsPageLocators.PRODUCT_CONTAINER)
        return len(products)
    
    def add_first_product_to_cart(self):
        for attempt in range(3):
            try:
                time.sleep(1)
                self.click_element(ProductsPageLocators.ADD_TO_CART_BUTTON)
                return
            except StaleElementReferenceException:
                time.sleep(1)
    
    def click_continue_shopping(self):
        time.sleep(1)
        self.click_element(ProductsPageLocators.CONTINUE_SHOPPING)