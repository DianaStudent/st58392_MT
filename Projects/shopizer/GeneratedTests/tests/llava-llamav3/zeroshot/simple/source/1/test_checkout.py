import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions import Key, ActionSequence
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

class TestShopifyCheckout(unittest.TestCase):
    def setUp(self):
        # Initialize the WebDriver with appropriate browser and options
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost/"

    def tearDown(self):
        # Close the WebDriver after testing
        self.driver.quit()

    def test_checkout_simple(self):
        # Open the checkout page
        self.driver.get(self.base_url)

        # Enter login credentials
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input = self.driver.find_element_by_id("email")
        email_input.send_keys("test22@user.com")

        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("test**11")

        # Click the 'Log in' button
        login_button = self.driver.find_element_by_css_selector("button.btn.login")
        self.wait_for_clickable(login_button)
        login_button.click()

        # Add products to the cart
        add_to_cart_button = self.driver.find_element_by_css_selector("a.cart-link")
        self.wait_for_clickable(add_to_cart_button)
        add_to_cart_button.click()

        # Go to the cart page
        cart_button = self.driver.find_element_by_css_selector("a.cart-link")
        self.wait_for_clickable(cart_button)
        cart_button.click()

        # Click 'Proceed to Checkout'
        proceed_button = self.driver.find_element_by_css_selector("button.checkout-button")
        self.wait_for_clickable(proceed_button)
        proceed_button.click()

        # Fill in the billing form
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "name"))
        )
        name_input = self.driver.find_element_by_id("name")
        name_input.send_keys("Mr. John Doe")

        address_input = self.driver.find_element_by_name("address1")
        address_input.send_keys("123 Main St, Anytown USA 12345")

        city_input = self.driver.find_element_by_name("city")
        city_input.send_keys("Anytown")
        state_input = self.driver.find_element_by_name("province")
        state_input.send_keys("CA")
        zip_code_input = self.driver.find_element_by_name("zip")
        zip_code_input.send_keys("12345")

        # Confirm success by verifying that the billing form is filled
        success_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='form-checkout-message']/span"))
        )
        self.assertEqual(success_message.text, "Thank you for your order.")

if __name__ == '__main__':
    unittest.main()