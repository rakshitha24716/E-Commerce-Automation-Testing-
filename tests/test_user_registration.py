"""Test cases for user registration and account management"""
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.test_data import BASE_URL, VALID_USER
import time

class TestUserRegistration:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
    
    @pytest.mark.smoke
    def test_user_login_successful(self):
        self.home_page.go_to_url(BASE_URL)
        self.home_page.click_signup_login()
        time.sleep(4)
        self.login_page.login_user(VALID_USER['email'], VALID_USER['password'])
        time.sleep(3)
        assert self.home_page.is_logout_visible(), "User should be logged in"
        self.home_page.take_screenshot("login_success")
    
    @pytest.mark.regression
    def test_login_with_invalid_credentials(self):
        self.home_page.go_to_url(BASE_URL)
        self.home_page.click_signup_login()
        time.sleep(4)
        self.login_page.login_user('invalid@example.com', 'wrongpassword')
        time.sleep(2)
        assert self.login_page.is_login_error_visible(), "Login error should be displayed"
    
    @pytest.mark.regression
    def test_logout_successful(self):
        self.home_page.go_to_url(BASE_URL)
        self.home_page.click_signup_login()
        time.sleep(4)
        self.login_page.login_user(VALID_USER['email'], VALID_USER['password'])
        time.sleep(3)
        self.home_page.click_logout()
        time.sleep(2)
        assert not self.home_page.is_logout_visible(), "User should be logged out"