"""Locators for all pages"""
from selenium.webdriver.common.by import By

class HomePageLocators:
    SIGNUP_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")
    LOGOUT_LINK = (By.XPATH, "//a[@href='/logout']")
    PRODUCTS_LINK = (By.XPATH, "//a[@href='/products']")
    CART_LINK = (By.XPATH, "//a[@href='/view_cart']")

class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    SIGNUP_NAME = (By.XPATH, "//input[@data-qa='signup-name']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(), 'Your email or password is incorrect')]")
    LOGIN_SUCCESS = (By.XPATH, "//a[@href='/logout']")

class ProductsPageLocators:
    PRODUCTS_TITLE = (By.XPATH, "//h2[contains(text(), 'All Products')]")
    PRODUCT_CONTAINER = (By.CLASS_NAME, "productinfo")
    ADD_TO_CART_BUTTON = (By.XPATH, "(//a[contains(text(), 'Add to cart')])[1]")
    CONTINUE_SHOPPING = (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")

class CartPageLocators:
    CART_ITEMS = (By.CLASS_NAME, "cart_quantity")
    REMOVE_ITEM = (By.CLASS_NAME, "cart_quantity_delete")
    PROCEED_CHECKOUT = (By.XPATH, "//a[contains(text(), 'Proceed To Checkout')]")
    EMPTY_CART_MESSAGE = (By.XPATH, "//b[contains(text(), 'Cart is empty')]")

class CheckoutPageLocators:
    PLACE_ORDER = (By.XPATH, "//a[contains(text(), 'Place Order')]")
    ORDER_CONFIRMATION = (By.XPATH, "//h2[contains(text(), 'Order Placed')]")