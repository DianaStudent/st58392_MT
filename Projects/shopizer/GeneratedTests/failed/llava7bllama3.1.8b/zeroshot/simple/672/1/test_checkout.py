from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_checkout_process(self):
        # Login
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'email')))
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'password')))
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'login-button')))

        email_input.send_keys('test22@user.com')
        password_input.send_keys('test**11')
        login_button.click()

        # Add products to cart
        product_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@class="product-btn"]')))
        for button in product_buttons:
            button.click()

        # Go to cart page
        cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'cart-button')))
        cart_button.click()

        # Proceed to checkout
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="proceed-to-checkout-btn"]')))
        proceed_to_checkout_button.click()

        # Fill in the billing form
        first_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'first-name')))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'last-name')))
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'email')))

        first_name_input.send_keys('John')
        last_name_input.send_keys('Doe')
        email_input.send_keys('john.doe@example.com')

        # Confirm success
        billing_form = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'billing-form')))
        self.assertTrue(billing_form.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()