from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost:8000/dk"

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        driver.get(self.base_url)
        
        # Step 1: Open home page - implicitly done by driver.get()

        # Step 2: Click the menu button ("Menu").
        menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 3: Click the "Store" link.
        store_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # Step 4: Click on the first product image (Thumbnail).
        first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@data-testid='product-wrapper']//img)[1]")))
        first_product.click()

        # Step 5: Select size by clicking the size button "L".
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 6: Add the product to the cart.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart.
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 8: Go to checkout, fill checkout fields.
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout form
        self.fill_checkout_fields(driver)

        # Step 9: Click "Continue to delivery"
        continue_to_delivery_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

        # Step 10: Select delivery method - radio button
        delivery_method_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-testid='radio-button'])[1]")))
        delivery_method_radio.click()

        # Step 11: Click "Continue to payment"
        continue_to_payment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        # Step 12: Select payment method - radio button
        payment_method_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-testid='radio-button'])[1]")))
        payment_method_radio.click()

        # Step 13: Click "Continue to review"
        continue_to_review_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-payment-button']")))
        continue_to_review_button.click()

        # Step 14: Click "Place Order".
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 15: Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Your order was placed successfully')]")))

        if not confirmation_message:
            self.fail("Confirmation message not found or empty.")

    def fill_checkout_fields(self, driver):
        wait = WebDriverWait(driver, 20)
        
        fields = [
            ("//input[@data-testid='shipping-first-name-input']", "user"),
            ("//input[@data-testid='shipping-last-name-input']", "test"),
            ("//input[@data-testid='shipping-address-input']", "street 1"),
            ("//input[@data-testid='shipping-postal-code-input']", "LV-1021"),
            ("//input[@data-testid='shipping-city-input']", "Riga"),
            ("//input[@data-testid='shipping-email-input']", "user@test.com"),
        ]

        for selector, value in fields:
            field = wait.until(EC.presence_of_element_located((By.XPATH, selector)))
            field.clear()
            field.send_keys(value)

        # Select country from combo box
        country_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-testid='shipping-country-select']")))
        country_select.click()
        country_options = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='dk']")))
        country_options.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()