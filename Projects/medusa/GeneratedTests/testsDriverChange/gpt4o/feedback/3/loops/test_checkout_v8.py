import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Open home page and click the menu button ("Menu")
        menu_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-menu-button']"))
        )
        menu_button.click()

        # Click the "Store" link
        store_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='store-link']"))
        )
        store_link.click()

        # Click on a product image (Thumbnail) - first product
        product_image = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-wrapper'] img"))
        )
        product_image.click()

        # Select size by clicking the size button "L"
        size_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='L']"))
        )
        size_button.click()

        # Add the product to the cart
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='add-product-button']"))
        )
        add_to_cart_button.click()

        # Click the cart button to open the cart
        cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-cart-link']"))
        )
        cart_button.click()

        # Wait for "Go to cart" button and click it
        go_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='go-to-cart-button']"))
        )
        go_to_cart_button.click()

        # Fill checkout fields
        self.fill_checkout_fields()

        # Continue to delivery
        continue_to_delivery_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='submit-address-button']"))
        )
        continue_to_delivery_button.click()

        # Select delivery method - radio button
        delivery_option_radio = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='delivery-option-radio']"))
        )[0]
        delivery_option_radio.click()

        # Continue to payment
        continue_to_payment_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='submit-delivery-option-button']"))
        )
        continue_to_payment_button.click()

        # Select payment method - radio button
        payment_option_radio = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='radio-button']"))
        )
        payment_option_radio.click()

        # Continue to review
        continue_to_review_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='submit-payment-button']"))
        )
        continue_to_review_button.click()

        # Place order
        place_order_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='submit-order-button']"))
        )
        place_order_button.click()

        # Verify the confirmation page contains "Your order was placed successfully"
        try:
            confirmation_text = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Your order was placed successfully.']"))
            )
            self.assertIsNotNone(confirmation_text)
        except TimeoutException:
            self.fail("Confirmation page did not load or success message not found.")

    def fill_checkout_fields(self):
        # Fill first name
        first_name_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-first-name-input']"))
        )
        first_name_input.clear()
        first_name_input.send_keys("user")

        # Fill last name
        last_name_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-last-name-input']"))
        )
        last_name_input.clear()
        last_name_input.send_keys("test")

        # Fill address
        address_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-address-input']"))
        )
        address_input.clear()
        address_input.send_keys("street 1")

        # Fill postal code
        postal_code_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-postal-code-input']"))
        )
        postal_code_input.clear()
        postal_code_input.send_keys("LV-1021")

        # Fill city
        city_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-city-input']"))
        )
        city_input.clear()
        city_input.send_keys("Riga")

        # Select country
        country_select = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-country-select']"))
        )
        country_select.click()
        country_option = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[value='dk']"))
        )
        country_option.click()

        # Fill email
        email_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-email-input']"))
        )
        email_input.clear()
        email_input.send_keys("user@test.com")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()