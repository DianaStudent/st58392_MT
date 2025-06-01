from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 2: Click the menu button ("Menu").
        menu_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='nav-menu-button']"))
        )
        menu_button.click()

        # Step 3: Click the "Store" link.
        store_link = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='store-link']"))
        )
        store_link.click()

        # Step 4: Click on a product image (Thumbnail) - first product.
        product_image = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//ul[@data-testid='products-list']//img"))
        )
        product_image.click()

        # Step 5: Select size by clicking the size button "L".
        size_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='product-options']//button[text()='L']"))
        )
        size_button.click()

        # Step 6: Add the product to the cart.
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button']"))
        )
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart.
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']"))
        )
        cart_button.click()

        # Wait for presence of "GO TO CHECKOUT" button
        go_to_checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']"))
        )
        go_to_checkout_button.click()

        # Step 8: Fill checkout fields
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-first-name-input']"))).send_keys("user")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-last-name-input']"))).send_keys("test")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-address-input']"))).send_keys("street 1")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-postal-code-input']"))).send_keys("LV-1021")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-city-input']"))).send_keys("Riga")
        country_select = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@data-testid='shipping-country-select']")))
        country_select.find_element(By.XPATH, "//option[@value='dk']").click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-email-input']"))).send_keys("user@test.com")

        # Step 9: Click "Continue to delivery"
        continue_to_delivery_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-address-button']"))
        )
        continue_to_delivery_button.click()

        # Step 10: Select delivery method - radio button
        delivery_radio_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@data-testid='radio-button'])[1]"))
        )
        delivery_radio_button.click()

        # Step 11: Click "Continue to payment"
        continue_to_payment_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-delivery-option-button']"))
        )
        continue_to_payment_button.click()

        # Step 12: Select payment method - radio button
        payment_radio_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@data-testid='radio-button'])[2]"))
        )
        payment_radio_button.click()

        # Step 13: Click "Continue to review"
        continue_to_review_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-payment-button']"))
        )
        continue_to_review_button.click()

        # Step 14: Click "Place Order".
        place_order_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']"))
        )
        place_order_button.click()

        # Step 15: Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_text = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']//span[text()='Your order was placed successfully.']"))
        )

        if not confirmation_text or not confirmation_text.text:
            self.fail("Confirmation message not found or empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()