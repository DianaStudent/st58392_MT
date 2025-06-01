from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # Open home page
        self.driver.get('http://localhost:3000/')

        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/product-category"]'))).click()
        
        # Select the first product
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="products list-unstyled"]/li[1]/a'))).click()

        # Click "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-action="cart-add"]'))).click()

        # Open shopping bag/cart
        self.driver.find_element(By.CSS_SELECTOR, '.cart-button').click()
        
        # Wait for "GO TO CHECKOUT" button to be present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[@class="btn checkout"]')))

        # Click "GO TO CHECKOUT"
        self.driver.find_element(By.XPATH, '//a[@class="btn checkout"]').click()

        # Fill required checkout fields
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'email')))
        email_input.send_keys('test@example.com')
        
        phone_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'phone')))
        phone_input.send_keys('1234567890')

        # Select shipping and payment method
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//label[@for="shipping_method_free"]'))).click()
        
        self.driver.find_element(By.XPATH, '//input[@id="payment_method_paypal"]').click()

        # Click "Next" button
        self.driver.find_element(By.XPATH, '//button[@data-action="checkout-next"]').click()
        
        # Click "Place Order"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary"]'))).click()

        # Confirm that success page contains message
        success_page = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//h1')))
        self.assertIn('Thanks for your order!', success_page.text)

if __name__ == '__main__':
    unittest.main()