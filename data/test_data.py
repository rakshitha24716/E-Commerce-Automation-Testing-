"""Test data"""

VALID_USER = {
    'name': 'Test User',
    'email': 'rakshitha_test_999@gmail.com',
    'password': 'Test@1234'
}

INVALID_USER = {
    'email': 'invalid@example.com',
    'password': 'WrongPassword'
}

SHIPPING_ADDRESS = {
    'first_name': 'John',
    'last_name': 'Doe',
    'company': 'Test Company',
    'address': '123 Test Street',
    'city': 'Test City',
    'state': 'Test State',
    'zipcode': '12345',
    'phone': '9876543210'
}

SEARCH_KEYWORDS = ['Blue Top', 'Stylish Dress', 'Winter Top']

BASE_URL = 'https://www.automationexercise.com'
PRODUCTS_URL = 'https://www.automationexercise.com/products'
CART_URL = 'https://www.automationexercise.com/view_cart'
