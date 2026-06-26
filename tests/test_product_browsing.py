"""Test cases for product browsing and search"""
import pytest
from pages.home_page import HomePage
from pages.product_page import ProductsPage
from data.test_data import BASE_URL, SEARCH_KEYWORDS
import time

class TestProductBrowsing:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.products_page = ProductsPage(driver)
    
    @pytest.mark.smoke
    def test_products_page_loads(self):
        self.home_page.go_to_url(BASE_URL)
        self.home_page.click_products()
        time.sleep(2)
        assert self.products_page.is_products_title_visible(), "Products page should load"
        self.home_page.take_screenshot("products_page")
    
    @pytest.mark.regression
    def test_product_count(self):
        self.home_page.go_to_url(BASE_URL)
        self.home_page.click_products()
        time.sleep(2)
        count = self.products_page.get_product_count()
        assert count > 0, "Products should be displayed"
    
    @pytest.mark.regression
    @pytest.mark.parametrize("keyword", SEARCH_KEYWORDS)
    def test_product_search(self, keyword):
        self.home_page.go_to_url(BASE_URL)
        self.home_page.click_products()
        time.sleep(2)
        self.products_page.search_product(keyword)
        time.sleep(2)
        count = self.products_page.get_product_count()
        assert count > 0, f"Search results for '{keyword}' should be found"