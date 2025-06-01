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

        # Step 1: Open home page
        # Step 2: Click the menu button ("Menu").
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 3: Click the "Store" link.
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 4: Click on a product image (Thumbnail) - first product.
        first_product_thumbnail = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Thumbnail']")))
        first_product_thumbnail.click()

        # Step 5: Select size by clicking the size button "L".
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 6: Add the product to the cart.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart.
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 8: Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout fields
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")
        address_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")
        postal_code_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")
        city_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")
        country_select = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
        email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        address_input.send_keys("street 1")
        postal_code_input.send_keys("LV-1021")
        city_input.send_keys("Riga")
        country_select.send_keys("Denmark")
        email_input.send_keys("user@test.com")

        continue_to_delivery_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
        continue_to_delivery_button.click()

        # Step 10: Select delivery method - radio button
        delivery_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']")))
        delivery_radio_button.click()

        # Step 11: Click "Continue to payment"
        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Step 12: Select payment method - radio button
        payment_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='radio-button']")))
        payment_radio_button.click()

        # Step 13: Click "Continue to review"
        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Step 14: Click "Place Order".
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 15: Verify the confirmation page contains "Your order was placed successfully".
        confirmation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Your order was placed successfully')]")))
        self.assertTrue("Your order was placed successfully" in confirmation_text.text, "Order was not placed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()