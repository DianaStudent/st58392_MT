from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class TestEcommerceFunctionality(unittest.TestCase):
    def setUp(self):
        # Set up ChromeDriver with the necessary options.
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

    def tearDown(self):
        # Close the browser after the test is completed.
        self.driver.quit()

    def test_ecommerce_functionality(self):
        # Navigate to the product page and add the product to cart.
        product_name = "book"
        product_page_url = f"https://www.example.com/{product_name}"
        self.product_page_url = product_page_url
        product_button = self.driver.find_element_by_xpath(f"//input[contains(@name, 'name') and contains(@value, '{product_name}')]/following::button[1]")
        product_button.click()

        # Click the shopping cart button.
        WebDriverWait(self.driver, 20).until(
            lambda driver: self.driver.find_element_by_id("shopping-cart-button").clickable
        )
        self.cart_button = self.driver.find_element_by_id("shopping-cart-button")

        # Use the "Checkout as Guest" option.
        guest_checkout_button = self.driver.find_element_by_id("guest-checkout")
        self.guest_checkout_button = guest_checkout_button

        # Confirm success by checking for an order completion message.
        order_completion_message = f"Order {order_number} completed successfully"
        WebDriverWait(self.driver, 20).until(
            lambda driver: self.driver.find_element_by_xpath(f"//*[contains(@class,'success-message') and contains(@id,'order-{order_number}')]/following::span[1]"))