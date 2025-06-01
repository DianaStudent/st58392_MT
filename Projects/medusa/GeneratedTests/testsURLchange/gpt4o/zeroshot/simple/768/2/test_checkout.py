import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to store
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//a[@data-testid="nav-store-link"]'))
            )
            store_link.click()
        except:
            self.fail("Store link not found")

        # Add first product to cart
        try:
            product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//a[@href="/dk/products/sweatshirt"]'))
            )
            product.click()
        except:
            self.fail("Product not found")

        # Select size and add to cart
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="L"]'))
            )
            size_button.click()

            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="add-product-button"]'))
            )
            add_to_cart_button.click()
        except:
            self.fail("Failed to add product or select size")

        # Go to cart
        try:
            cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="nav-cart-link"]'))
            )
            cart_link.click()
        except:
            self.fail("Cart link not found")

        # Proceed to checkout
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="go-to-cart-button"]'))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Go to checkout button not found")

        # Fill checkout information
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//input[@data-testid="shipping-email-input"]'))
            )
            email_input.send_keys("user@test.com")
            
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//select[@data-testid="shipping-country-select"]'))
            )
            country_select.click()

            country_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//option[@value="dk"]'))
            )
            country_option.click()
            
            continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit-address-button"]'))
            )
            continue_button.click()
        except:
            self.fail("Failed to fill checkout information")

        # Select delivery method
        try:
            delivery_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit-delivery-option-button"]'))
            )
            delivery_option.click()
        except:
            self.fail("Failed to select delivery option or proceed")

        # Select payment method
        try:
            payment_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit-payment-button"]'))
            )
            payment_option.click()
        except:
            self.fail("Failed to select payment option or proceed")

        # Place the order
        try:
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="submit-order-button"]'))
            )
            place_order_button.click()
        except:
            self.fail("Failed to place order")

        # Verify order success
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//span[text()="Your order was placed successfully."]'))
            )
            self.assertTrue(success_message.is_displayed(), "Order success message not displayed")
        except:
            self.fail("Order success message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()