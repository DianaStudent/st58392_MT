from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='menu-button']")))

    def test_checkout_process(self):
        # Click the menu button ("Menu").
        menu_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='menu-button']")))
        menu_button.click()

        # Click the "Store" link.
        store_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/store']")))
        store_link.click()

        # Click on a product image (Thumbnail) - first product.
        thumbnail = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@data-testid='thumbnail']")))
        thumbnail.click()

        # Select size by clicking the size button "L".
        size_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='size-button-L']")))
        size_button.click()

        # Add the product to the cart.
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-to-cart']")))
        add_to_cart_button.click()

        # Explicitly click the cart button to open the cart.
        cart_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='cart-button']")))
        cart_button.click()

        # Click "Go to checkout", fill checkout fields:
        go_to_checkout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-checkout']")))
        go_to_checkout_button.click()
        
        first_name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='first-name']")))
        last_name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='last-name']")))
        email_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='email']")))
        shipping_address_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-address']")))

        first_name_field.send_keys("user")
        last_name_field.send_keys("test")
        email_field.send_keys("user@test.com")
        shipping_address_field.send_keys("street 1")

        # Click "Continue to delivery"
        continue_to_delivery_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='continue-to-delivery']")))
        continue_to_delivery_button.click()

        # Select delivery method - radio button
        delivery_method_radio_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @name='delivery-method']")))
        delivery_method_radio_button.click()

        # Click "Continue to payment"
        continue_to_payment_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='continue-to-payment']")))
        continue_to_payment_button.click()

        # Select payment method - radio button
        payment_method_radio_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @name='payment-method']")))
        payment_method_radio_button.click()

        # Click "Continue to review"
        continue_to_review_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='continue-to-review']")))
        continue_to_review_button.click()

        # Click "Place Order".
        place_order_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='place-order']")))
        place_order_button.click()

        # Verify the confirmation page contains: "Your order was placed successfully"
        success_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[@data-testid='success-text']"))).text
        self.assertEqual(success_text, "Your order was placed successfully", "Order not placed successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()