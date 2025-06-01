from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page (Already done in setUp)

        # Step 2: Click the menu button ("Menu")
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        menu_button.click()

        # Step 3: Click the "Store" link.
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
        store_link.click()

        # Step 4: Click on a product image (Thumbnail) - first product.
        product_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="product-wrapper"] img')))
        product_image.click()

        # Step 5: Select size by clicking the size button "L".
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="L"]')))
        size_button.click()

        # Step 6: Add the product to the cart.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="add-product-button"]')))
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart.
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_button.click()

        # Step 8: Click "Go to checkout", fill checkout fields
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="go-to-cart-button"]')))
        go_to_checkout_button.click()

        # Fill in checkout fields
        self.fill_checkout_fields()

        # Step 9: Click "Continue to delivery"
        continue_to_delivery_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-address-button"]')))
        continue_to_delivery_button.click()

        # Step 10: Select delivery method - radio button
        delivery_method_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-testid="delivery-option-radio"] button')))
        delivery_method_radio.click()

        # Step 11: Click "Continue to payment"
        continue_to_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-delivery-option-button"]')))
        continue_to_payment_button.click()

        # Step 12: Select payment method - radio button
        payment_method_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[id^="headlessui-radio-"] button')))
        payment_method_radio.click()

        # Step 13: Click "Continue to review"
        continue_to_review_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-payment-button"]')))
        continue_to_review_button.click()

        # Step 14: Click "Place Order".
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-order-button"]')))
        place_order_button.click()

        # Step 15: Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Your order was placed successfully")]')))
        if not confirmation_message:
            self.fail("Order confirmation message not found.")

    def fill_checkout_fields(self):
        driver = self.driver

        # Fill First name
        first_name = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-first-name-input"]')
        first_name.send_keys("user")

        # Fill Last name
        last_name = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-last-name-input"]')
        last_name.send_keys("test")

        # Fill Address
        address = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-address-input"]')
        address.send_keys("street 1")

        # Fill Postal code
        postal_code = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-postal-code-input"]')
        postal_code.send_keys("LV-1021")

        # Fill City
        city = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-city-input"]')
        city.send_keys("Riga")

        # Select Country
        country_select = driver.find_element(By.CSS_SELECTOR, 'select[data-testid="shipping-country-select"]')
        country_select.send_keys("Denmark")

        # Fill Email
        email = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-email-input"]')
        email.send_keys("user@test.com")

if __name__ == "__main__":
    unittest.main()