import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page
        home_title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertIsNotNone(home_title)
        self.assertIn("Ecommerce Starter Template", home_title.text)

        # 2. Click the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-menu-button']")))
        menu_button.click()

        # 3. Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='store-link']")))
        store_link.click()

        # 4. Click on a product image (Thumbnail) - first product
        product_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='product-wrapper'] img")))
        product_image.click()

        # 5. Select size by clicking the size button "L"
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # 6. Add the product to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # 7. Explicitly click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        cart_button.click()

        go_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='go-to-cart-button']")))
        self.assertIsNotNone(go_to_cart_button)

        # 8. Click "Go to checkout", fill checkout fields
        go_to_cart_button.click()

        # Fill in checkout fields
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-first-name-input']"))).send_keys("user")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-city-input']").send_keys("Riga")
        
        country_select = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-country-select']")))
        country_select.find_element(By.XPATH, "//option[text()='Denmark']").click()

        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-email-input']").send_keys("user@test.com")

        # 9. Click "Continue to delivery"
        submit_address_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-address-button']")
        submit_address_button.click()

        # 10. Select delivery method - radio button
        delivery_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#headlessui-radio-\\:rh\\: button")))
        delivery_radio_button.click()

        # 11. Click "Continue to payment"
        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # 12. Select payment method - radio button
        payment_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#headlessui-radio-\\:rk\\: button")))
        payment_radio_button.click()

        # 13. Click "Continue to review"
        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # 14. Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='submit-order-button']")))
        place_order_button.click()

        # 15. Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']")))
        self.assertIsNotNone(confirmation_message)

if __name__ == "__main__":
    unittest.main()