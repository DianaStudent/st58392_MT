import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckout(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.get('http://localhost:3000/')

    def tearDown(self):
        self.driver.quit()

    def test_checkout_flow(self):
        # Add a product to the cart
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add to Cart')]")

        # Wait for presence of "GO TO CHECKOUT" button and click on it
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'GO TO CHECKOUT')]")))
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("test@example.com")

        phone_number_field = self.driver.find_element(By.NAME, "phone")
        phone_number_field.send_keys("1234567890")

        shipping_address_field = self.driver.find_element(By.NAME, "shippingAddress")
        shipping_address_field.send_keys("123 Main St")

        # Select a shipping method
        shipping_method_dropdown = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@name='shippingMethod']")))
        shipping_method_dropdown.click()

        # Select a payment method
        payment_method_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Pay with Card')]")))
        payment_method_button.click()

        # Place the order
        place_order_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Place Your Order')]")))
        place_order_button.click()

        # Confirm that the final success page contains the text "Thanks for your order!"
        self.assertEqual("Thanks for your order!", WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1"))).text)

if __name__ == '__main__':
    unittest.main()