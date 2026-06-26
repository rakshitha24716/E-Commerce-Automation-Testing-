"""Checkout page object"""
from pages.base_page import BasePage
from data.locators import CheckoutPageLocators

class CheckoutPage(BasePage):
    
    def click_place_order(self):
        self.click_element(CheckoutPageLocators.PLACE_ORDER)
    
    def is_order_confirmed(self):
        return self.is_element_visible(CheckoutPageLocators.ORDER_CONFIRMATION)