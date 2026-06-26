"""Login page object"""
from pages.base_page import BasePage
from data.locators import LoginPageLocators

class LoginPage(BasePage):
    
    def enter_login_email(self, email):
        self.send_text(LoginPageLocators.LOGIN_EMAIL, email)
    
    def enter_login_password(self, password):
        self.send_text(LoginPageLocators.LOGIN_PASSWORD, password)
    
    def click_login_button(self):
        element = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
    
    def login_user(self, email, password):
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.click_login_button()
    
    def enter_signup_name(self, name):
        self.send_text(LoginPageLocators.SIGNUP_NAME, name)
    
    def enter_signup_email(self, email):
        self.send_text(LoginPageLocators.SIGNUP_EMAIL, email)
    
    def click_signup_button(self):
        self.click_element(LoginPageLocators.SIGNUP_BUTTON)
    
    def signup_user(self, name, email):
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.click_signup_button()
    
    def is_login_error_visible(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_ERROR)
    
    def is_login_successful(self):
        return self.is_element_visible(LoginPageLocators.LOGIN_SUCCESS)