import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Step 1: Click the menu button.
            menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
            menu_button.click()

            # Step 2: Click the "Store" link.
            store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
            store_link.click()

            # Step 3: Click on a product image (Thumbnail) - first product.
            first_product_thumbnail = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[data-testid='products-list'] li:first-child img[alt='Thumbnail']")))
            first_product_thumbnail.click()

            # Step 4: Select size by clicking the size button "L".
            size_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']:nth-child(1)")))
            size_button.click()

            # Step 5: Add the product to the cart.
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
            add_to_cart_button.click()

            # Step 6: Explicitly click the cart button.
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
            cart_button.click()

            # Step 7: Click "Go to checkout"
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='checkout-button']")))
            go_to_checkout_button.click()

            # Step 8: Fill checkout fields
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys("user")
            driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys("test")
            driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys("street 1")
            driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
            driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys("Riga")
            country_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
            country_select.send_keys("Denmark")
            driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys("user@test.com")

            continue_to_delivery_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
            continue_to_delivery_button.click()

            # Step 9: Select delivery method - radio button
            delivery_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']")))
            delivery_radio_button.click()

            # Step 10: Click "Continue to payment"
            continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
            continue_to_payment_button.click()

            # Step 11: Select payment method - radio button
            payment_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='radio-button']")))
            payment_radio_button.click()

            # Step 12: Click "Continue to review"
            continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
            continue_to_review_button.click()

            # Step 13: Click "Place Order".
            place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
            place_order_button.click()

            # Step 14: Verify the confirmation page contains "Your order was placed successfully".
            confirmation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[contains(text(),'Your order was placed successfully')]")))
            self.assertTrue("Your order was placed successfully" in confirmation_text.text, "Order was not placed successfully.")
        
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()