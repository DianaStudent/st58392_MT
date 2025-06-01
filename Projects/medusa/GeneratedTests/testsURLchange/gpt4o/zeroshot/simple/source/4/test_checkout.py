from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class MedusaStoreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open the store page
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-store-link']"))).click()
        
        # Select a product
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Medusa Sweatshirt']/ancestor::a"))).click()
        
        # Select size
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']"))).click()
        
        # Add to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if add_to_cart_button.text != "Add to cart":
            self.fail("Add to cart button not available or wrong state")

        add_to_cart_button.click()
        
        # Go to cart
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))).click()

        # Proceed to checkout
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']"))).click()

        # Fill in shipping details
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys("User")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys("Test")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys("Street 1")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys("Riga")
        driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']").send_keys("Denmark")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys("user@test.com")

        # Continue to delivery
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']"))).click()

        # Choose delivery option
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Express Shipping')]"))).click()
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']").click()

        # Choose payment method
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Manual Payment']"))).click()
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']").click()

        # Confirm order
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))).click()

        # Verify success message
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Your order was placed successfully')]")))
        self.assertIsNotNone(success_message, "Order completion message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()