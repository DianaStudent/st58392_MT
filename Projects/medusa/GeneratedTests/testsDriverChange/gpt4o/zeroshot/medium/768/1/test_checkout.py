import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        driver.get("http://localhost:8000/dk")

        # Step 2: Click on the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 3: Click on the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='store-link']")))
        store_link.click()

        # Step 4: Click on a product image (thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='product-wrapper']")))
        product_image.click()

        # Step 5: Select a size
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 6: Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        if "Out of stock" in add_to_cart_button.text:
            self.fail("Product is out of stock")
        add_to_cart_button.click()

        # Step 7: Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 8: Go to checkout and fill checkout fields
        go_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='go-to-cart-button']")))
        go_to_cart_button.click()

        # Fill in checkout fields
        self.fill_checkout_fields()

        # Step 9: Select delivery and payment methods
        self.select_delivery_and_payment()

        # Step 10: Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 11: Verify the confirmation page
        confirmation_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Your order was placed successfully')]"))
        )
        if not confirmation_message:
            self.fail("Order confirmation message not found")

    def fill_checkout_fields(self):
        driver = self.driver

        # Fill personal information
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-first-name-input']").send_keys("user")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-city-input']").send_keys("Riga")

        # Select Country
        country_select = driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-country-select']")
        country_select.click()
        wait = WebDriverWait(driver, 20)
        denmark_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='dk']")))
        denmark_option.click()

        # Fill email
        driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-email-input']").send_keys("user@test.com")

        # Continue to delivery
        continue_to_delivery_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-address-button']")
        continue_to_delivery_button.click()

    def select_delivery_and_payment(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Select delivery method
        delivery_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Express Shipping']"))
        )
        delivery_option.click()
        
        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Select payment method
        payment_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Manual Payment']"))
        )
        payment_option.click()

        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-payment-button']")
        continue_to_review_button.click()

if __name__ == "__main__":
    unittest.main()