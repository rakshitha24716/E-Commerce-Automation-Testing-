"""Test cases for checkout process"""
import pytest
from pages.home_page import HomePage
from pages.product_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from data.test_data import BASE_URL
import time

class TestCheckout:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.products_page = ProductsPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
    
    @pytest.mark.smoke
    def test_proceed_to_checkout(self):
        self.home_page.go_to_url(BASE_URL)
        self.home_page.click_products()
        time.sleep(2)
        self.products_page.add_first_product_to_cart()
        time.sleep(2)
        self.products_page.click_continue_shopping()
        time.sleep(1)
        self.home_page.click_cart()
        time.sleep(2)
        count = self.cart_page.get_cart_items_count()
        assert count > 0, "Cart should have items before checkout"
        self.home_page.take_screenshot("ready_for_checkout")