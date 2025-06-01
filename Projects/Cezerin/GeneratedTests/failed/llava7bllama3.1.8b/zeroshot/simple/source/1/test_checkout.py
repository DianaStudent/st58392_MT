from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # Navigate to the URL
        self.driver.get("http://localhost:3000/")

        # Add a product to cart and click on cart button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "add-to-cart"))).click()
        self.driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()

        # Wait for presence of "GO TO CHECKOUT" button using html_data
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='go-to-checkout']"))).click()
        
        # Fill required checkout fields
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
        self.driver.find_element(By.ID, "phone").send_keys("1234567890")

        # Select shipping address and shipping method
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='shipping-address']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='shipping-method']"))).click()

        # Select payment method
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='payment-method']"))).click()
        
        # Place order and confirm that the final success page contains "Thanks for your order!"
        self.driver.find_element(By.XPATH, "//button[@class='place-order']").click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Thanks for your order!')]")))

if __name__ == '__main__':
    unittest.main()