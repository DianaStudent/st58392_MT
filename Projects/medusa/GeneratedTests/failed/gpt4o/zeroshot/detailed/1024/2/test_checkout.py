from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        driver.get("http://localhost:8000/dk")

        # Step 2: Click the menu button ("Menu")
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 3: Click the "Store" link.
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 4: Click on the product image (Thumbnail) - first product.
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a")))
        first_product.click()

        # Step 5: Select size by clicking the size button "L".
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 6: Add the product to the cart.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if add_to_cart_button.text != "Add to cart":
            self.fail("Add to cart button not available")
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart.
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 8: Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout fields
        self.fill_checkout_fields()

        # Step 9: Click "Continue to delivery"
        continue_to_delivery_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

        # Step 10: Select delivery method - radio button
        delivery_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button[data-testid='radio-button']")))
        delivery_radio_button.click()

        # Step 11: Click "Continue to payment"
        continue_to_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        # Step 12: Select payment method - radio button
        payment_radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id^='headlessui-radio'] button[data-testid='radio-button']")))
        payment_radio_button.click()

        # Step 13: Click "Continue to review"
        continue_to_review_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        continue_to_review_button.click()

        # Step 14: Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 15: Verify the confirmation page contains: "Your order was placed successfully"
        self.verify_order_success()

    def fill_checkout_fields(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys("user")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys("Riga")
        
        country_dropdown = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
        actions = ActionChains(driver)
        actions.click(country_dropdown).perform()
        country_option = driver.find_element(By.XPATH, "//option[@value='dk']")
        actions.click(country_option).perform()

        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys("user@test.com")

    def verify_order_success(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        order_success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your order was placed successfully')]")))
        if not order_success_message:
            self.fail("Order success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()