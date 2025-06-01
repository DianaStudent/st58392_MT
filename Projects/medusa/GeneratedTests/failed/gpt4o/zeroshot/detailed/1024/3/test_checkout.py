from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MedusaCheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page and click the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2: Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on a product image (first product)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-wrapper'] img")))
        product_image.click()

        # Step 4: Select size "L" by clicking the size button
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 5: Add the product to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        if add_to_cart_button.text == "Out of stock":
            self.fail("Add to cart button is disabled (Out of stock)")
        add_to_cart_button.click()

        # Step 6: Explicitly click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7: Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Step 8: Fill checkout fields
        self._fill_checkout_fields()

        # Step 9: Click "Continue to delivery"
        continue_delivery_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='submit-address-button']")))
        continue_delivery_button.click()

        # Step 10: Select delivery method - radio button
        delivery_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='delivery-option-radio']")))
        delivery_radio_button.click()

        # Step 11: Click "Continue to payment"
        continue_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='submit-delivery-option-button']")))
        continue_payment_button.click()

        # Step 12: Select payment method - radio button
        payment_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='radio-button']")))
        payment_radio_button.click()

        # Step 13: Click "Continue to review"
        continue_review_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='submit-payment-button']")))
        continue_review_button.click()

        # Step 14: Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 15: Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']")))
        if not confirmation_message:
            self.fail("Confirmation message not found or is empty.")

    def _fill_checkout_fields(self):
        driver = self.driver
        wait = self.wait

        # First name
        first_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='shipping-first-name-input']")))
        first_name_input.send_keys("user")

        # Last name
        last_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='shipping-last-name-input']")))
        last_name_input.send_keys("test")

        # Address
        address_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='shipping-address-input']")))
        address_input.send_keys("street 1")

        # Postal code
        postal_code_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='shipping-postal-code-input']")))
        postal_code_input.send_keys("LV-1021")

        # City
        city_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='shipping-city-input']")))
        city_input.send_keys("Riga")

        # Country
        country_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-country-select']")))
        country_select.click()
        denmark_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='dk']")))
        denmark_option.click()

        # Email
        email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='shipping-email-input']")))
        email_input.send_keys("user@test.com")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()