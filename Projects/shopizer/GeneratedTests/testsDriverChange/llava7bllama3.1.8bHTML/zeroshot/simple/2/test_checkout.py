from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_checkout_process(self):
        # Navigate to the checkout page
        self.driver.get('http://localhost/checkout')

        # Login to the application
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))).send_keys("test22@user.com")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))).send_keys("test**11")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()

        # Add products to the cart
        self.driver.get('http://localhost/cart')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[@title="Add to Cart"]'))).click()
        
        # Go to cart page and click "Proceed to Checkout"
        self.driver.get('http://localhost/cart')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary checkout-button"]'))).click()

        # Fill in the billing form
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@name="first_name"]'))).send_keys('John')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@name="last_name"]'))).send_keys('Doe')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@name="address1"]'))).send_keys('123 Main St')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@name="city"]'))).send_keys('Anytown')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//select[@name="state_id"]'))).send_keys('CA')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@name="postcode"]'))).send_keys('12345')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//select[@name="country_id"]'))).send_keys('USA')
        
        # Confirm success by verifying that the billing form is filled
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//input[@name="first_name"]'), 'John')))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//input[@name="last_name"]'), 'Doe')))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//input[@name="address1"]'), '123 Main St')))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//input[@name="city"]'), 'Anytown')))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//select[@name="state_id"]'), 'CA')))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//input[@name="postcode"]'), '12345')))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//select[@name="country_id"]'), 'USA')))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()