"""Cart page object"""
from pages.base_page import BasePage
from data.locators import CartPageLocators

class CartPage(BasePage):
    
    def get_cart_items_count(self):
        items = self.driver.find_elements(*CartPageLocators.CART_ITEMS)
        return len(items)
    
    def remove_item_from_cart(self):
        self.click_element(CartPageLocators.REMOVE_ITEM)
    
    def is_cart_empty(self):
        return self.is_element_visible(CartPageLocators.EMPTY_CART_MESSAGE)
    
    def click_proceed_checkout(self):
        self.click_element(CartPageLocators.PROCEED_CHECKOUT)