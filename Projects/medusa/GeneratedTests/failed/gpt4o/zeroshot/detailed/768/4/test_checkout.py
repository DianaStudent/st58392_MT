from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure the ChromeDriver is in PATH or provide the executable path
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # 1. Click the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 2. Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 3. Click on the first product image
        product_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[data-testid='products-list'] li:first-child img")))
        product_image.click()

        # 4. Select size "L"
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # 5. Add the product to the cart
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_text = add_to_cart_btn.text.strip()
        if not add_to_cart_text or add_to_cart_text != "Add to cart":
            self.fail("Expected 'Add to cart' button not found.")
        add_to_cart_btn.click()

        # 6. Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # 7. Click "Go to checkout"
        go_to_checkout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_btn.click()

        # 8. Fill checkout fields
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys("user")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']"))).send_keys("test")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']"))).send_keys("street 1")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']"))).send_keys("LV-1021")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']"))).send_keys("Riga")
        country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
        country_select.find_element(By.XPATH, "//option[@value='dk']").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))).send_keys("user@test.com")

        # 9. Click "Continue to delivery"
        continue_to_delivery_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        continue_to_delivery_btn.click()

        # 10. Select delivery method
        delivery_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button")))
        delivery_radio_button.click()

        # 11. Click "Continue to payment"
        continue_to_payment_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        continue_to_payment_btn.click()

        # 12. Select payment method
        payment_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id^='headlessui-radio-'] button[data-testid='radio-button']")))
        payment_radio_button.click()

        # 13. Click "Continue to review"
        continue_to_review_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        continue_to_review_btn.click()

        # 14. Click "Place Order".
        place_order_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_btn.click()

        # 15. Verify the success page message
        confirmation_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='order-complete-container'] h1 span:nth-child(2)")))
        confirmation_text = confirmation_message.text.strip()
        if not confirmation_text or confirmation_text != "Your order was placed successfully.":
            self.fail("Order confirmation message not found or incorrect.")

if __name__ == "__main__":
    unittest.main()