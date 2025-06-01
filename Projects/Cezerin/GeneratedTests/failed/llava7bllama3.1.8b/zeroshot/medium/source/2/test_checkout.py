from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def test_checkout_process(self):
        # Click on product category
        category_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category']")))
        category_link.click()

        # Select the first product
        product_name = self.driver.find_element(By.XPATH, "//h2").text
        product_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{product_name}')]")))
        product_button.click()

        # Click "Add to cart"
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[@onclick='addToCart()']")
        add_to_cart_button.click()

        # Click the shopping cart icon
        cart_icon = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='cart-button']")))
        cart_icon.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        checkout_button = self.driver.find_element(By.XPATH, "//a[@href='/checkout']")
        self.assertIsNotNone(checkout_button)

        # Click the "GO TO CHECKOUT" button
        checkout_button.click()

        # Fill required checkout fields
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']")))
        phone_input = self.driver.find_element(By.XPATH, "//input[@name='phone']")
        shipping_address_input = self.driver.find_element(By.XPATH, "//textarea[@name='shippingAddress']")
        select_shipping_method_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Select Shipping Method')]")))
        payment_method_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Payment Method')]")

        email_input.send_keys("test@example.com")
        phone_input.send_keys("1234567890")
        shipping_address_input.send_keys("123 Main St")
        select_shipping_method_button.click()
        payment_method_button.click()

        # Select a shipping and payment method
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]"))).click()

        # Confirm that the final success page contains the text: "Thanks for your order!"
        success_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='success-message']")))
        self.assertEqual(success_message.text, "Thanks for your order!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()