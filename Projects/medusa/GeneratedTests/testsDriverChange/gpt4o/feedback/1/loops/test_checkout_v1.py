import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MedusaStoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click the menu button
        nav_menu_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='nav-menu-button']")))
        nav_menu_button.click()

        # Step 2: Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on first product image (Thumbnail)
        first_product_image = wait.until(EC.element_to_be_clickable((By.XPATH, "(//ul[@data-testid='products-list']//a)[1]")))
        first_product_image.click()

        # Step 4: Select size "L"
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
        size_button.click()

        # Step 5: Add the product to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Step 6: Click the cart button
        cart_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_link.click()

        # Step 7: Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout fields
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-first-name-input']"))).send_keys("user")
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-last-name-input']"))).send_keys("test")
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-address-input']"))).send_keys("street 1")
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-postal-code-input']"))).send_keys("LV-1021")
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-city-input']"))).send_keys("Riga")
        wait.until(EC.presence_of_element_located((By.XPATH, "//select[@data-testid='shipping-country-select']"))).send_keys("Denmark")

        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-email-input']")))
        email_input.clear()
        email_input.send_keys("user@test.com")

        # Step 8: Continue to delivery
        continue_to_delivery_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

        # Step 9: Select delivery method
        delivery_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio'][1]//button[@data-testid='radio-button']")))
        delivery_option.click()

        # Step 10: Continue to payment
        continue_to_payment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        # Step 11: Select payment method
        payment_method = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='headlessui-radio-:rk:']//button[@data-testid='radio-button']")))
        payment_method.click()

        # Step 12: Continue to review
        continue_to_review_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-payment-button']")))
        continue_to_review_button.click()

        # Step 13: Place Order
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 14: Verify confirmation
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your order was placed successfully')]")))
        if not confirmation_message.is_displayed():
            self.fail("Confirmation message not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()