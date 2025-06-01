from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Ecommerce Starter Template')]")))

        # 2. Click on the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 3. Click on the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 4. Click on a product image (thumbnail)
        product_image = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@data-testid='products-list']//img[@alt='Thumbnail']")))
        product_image.click()

        # 5. Select a size
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # 6. Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # 7. Click the cart button to open the cart
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_link.click()

        # 8. Click "Go to checkout", fill checkout fields
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        self.fill_checkout_fields(wait)

        # 9. Select delivery and payment methods
        self.select_delivery_and_payment(wait)

        # 10. Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # 11. Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Your order was placed successfully')]")))
        self.assertTrue(confirmation_text.is_displayed(), "Confirmation text not found or not visible.")

    def fill_checkout_fields(self, wait):
        checkout_fields = [
            ("shipping-first-name-input", "user"),
            ("shipping-last-name-input", "test"),
            ("shipping-address-input", "street 1"),
            ("shipping-postal-code-input", "LV-1021"),
            ("shipping-city-input", "Riga"),
            ("shipping-email-input", "user@test.com")
        ]

        for test_id, value in checkout_fields:
            input_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"input[data-testid='{test_id}']")))
            if not input_element:
                self.fail(f"Input field with test_id='{test_id}' not found.")
            input_element.clear()
            input_element.send_keys(value)

        country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
        country_select.send_keys("Denmark")

        billing_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='billing-address-checkbox']")))
        billing_checkbox.click()

        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        continue_button.click()

    def select_delivery_and_payment(self, wait):
        express_shipping = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Express Shipping')]")))
        express_shipping.click()

        continue_to_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        manual_payment = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Manual Payment')]")))
        manual_payment.click()

        continue_to_review_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        continue_to_review_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()