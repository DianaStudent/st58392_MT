from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to Category A
        category_a_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
        )
        category_a_link.click()
        
        # Click on Product A
        product_a_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
        )
        product_a_link.click()
        
        # Add Product A to cart
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button-addtocart"))
        )
        add_to_cart_button.click()
        
        # Click on the cart button
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
        )
        cart_button.click()
        
        # Wait for "GO TO CHECKOUT" button to appear and click it
        go_to_checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "GO TO CHECKOUT"))
        )
        go_to_checkout_button.click()
        
        # Fill Checkout Details
        email_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )
        email_input.send_keys("mail@mail.com")

        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")
        
        # Select shipping method
        shipping_method = driver.find_element(By.NAME, "shipping_method_id")
        shipping_method.click()
        
        # Select payment method
        payment_method = driver.find_element(By.NAME, "payment_method_id")
        payment_method.click()
        
        # Click on "Next" button in checkout
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()
        
        # Click on "Place Order" button
        place_order_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))
        )
        place_order_button.click()
        
        # Verify success page contains "Thanks for your order!"
        success_message = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
        )
        self.assertIn("Thanks for your order!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()