from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class CheckoutAutomationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')  # Use local path to the home page HTML file
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Test Scenario Steps

        # 1. Open home page (already opened in setUp)
        # No explicit step

        # 2. Click on product category.
        category_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='primary-nav']//a[@href='/category-a']")))
        category_link.click()
        
        # Wait for category page to load
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='category-title' and text()='Category A']")))

        # 3. Select the first product.
        first_product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        first_product.click()
        
        # Wait for product page to load
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='product-name' and text()='Product A']")))

        # 4. Click the "Add to cart" button.
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button is-success is-fullwidth']")))
        add_to_cart_btn.click()

        # 5. Click the cart icon/button to open the shopping bag.
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']/img[@title='cart']")))
        cart_icon.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button is-primary is-fullwidth has-text-centered' and text()='Go to checkout']")))
        self.assertTrue(go_to_checkout_btn.is_displayed(), "GO TO CHECKOUT button is not displayed.")

        # 7. Click the "GO TO CHECKOUT" button.
        go_to_checkout_btn.click()

        # 8. Fill required checkout fields
        self.wait.until(EC.element_to_be_clickable((By.ID, "customer.email"))).send_keys("mail@mail.com")
        self.wait.until(EC.element_to_be_clickable((By.ID, "customer.mobile"))).send_keys("12345678")
        self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.country"))).clear()
        self.wait.until(EC.element_to_be_clickable((By.ID, "shipping_address.country"))).send_keys("SG")
        self.wait.until(EC.element_to_be_clickable((By.ID, "shipping_address.state"))).send_keys("Riga")
        self.wait.until(EC.element_to_be_clickable((By.ID, "shipping_address.city"))).send_keys("Riga")

        # 9. Select a shipping and payment method.
        shipping_method = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='shipping_method_id' and @value='67ca982ef38a654a7c2c1a69']")))
        self.assertTrue(shipping_method.is_displayed(), "Shipping method is not displayed.")
        shipping_method.click()

        payment_method = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='payment_method_id' and @value='67ca982ef38a654a7c2c1a6a']")))
        self.assertTrue(payment_method.is_displayed(), "Payment method is not displayed.")
        payment_method.click()

        # 10. Click "Next" and then "Place Order" to complete the process.
        next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='checkout-button button is-primary' and @type='submit']")))
        next_button.click()

        # Wait for Shipping page
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='checkout-button button is-primary' and text()='Place Order']")))
        place_order_button.click()

        # 11. Confirm that the success page contains the message: "Thanks for your order!".
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='checkout-success-title' and contains(text(),'Thanks for your order!')]")))
        self.assertTrue(success_message.is_displayed(), "Order success message is not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()