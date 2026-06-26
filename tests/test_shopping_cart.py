"""Test cases for shopping cart"""
import pytest
from pages.home_page import HomePage
from pages.product_page import ProductsPage
from pages.cart_page import CartPage
from data.test_data import BASE_URL
import time

class TestShoppingCart:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.products_page = ProductsPage(driver)
        self.cart_page = CartPage(driver)
    
    @pytest.mark.smoke
    def test_add_product_to_cart(self):
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
        assert count > 0, "Product should be in cart"
        self.home_page.take_screenshot("product_added_to_cart")
    
    @pytest.mark.regression
    def test_remove_product_from_cart(self):
        self.home_page.go_to_url(BASE_URL)
        self.home_page.click_products()
        time.sleep(2)
        self.products_page.add_first_product_to_cart()
        time.sleep(2)
        self.products_page.click_continue_shopping()
        time.sleep(1)
        self.home_page.click_cart()
        time.sleep(2)
        self.cart_page.remove_item_from_cart()
        time.sleep(2)
        assert self.cart_page.is_cart_empty(), "Cart should be empty"