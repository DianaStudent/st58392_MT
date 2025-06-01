import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to store
        store_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-store-link']")))
        store_link.click()

        # Select a product
        product_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/dk/products/sweatshirt']")))
        product_link.click()

        # Select size and add to cart
        size_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='L']")))
        size_button.click()

        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Go to cart
        cart_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_link.click()

        # Go to checkout
        checkout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        checkout_button.click()

        # Fill address form
        first_name_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-first-name-input']")))
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-last-name-input']")
        last_name_input.send_keys("test")

        address_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-address-input']")
        address_input.send_keys("street 1")

        postal_code_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-postal-code-input']")
        postal_code_input.send_keys("LV-1021")

        city_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-city-input']")
        city_input.send_keys("Riga")

        country_select = driver.find_element(By.XPATH, "//select[@data-testid='shipping-country-select']")
        country_select.send_keys("Denmark")

        email_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-email-input']")
        email_input.send_keys("user@test.com")

        continue_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-address-button']")
        continue_button.click()

        # Select delivery option
        delivery_option = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='delivery-option-radio']//button[text()='Express Shipping']")))
        delivery_option.click()
        
        continue_to_payment_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Select payment method
        payment_option = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='radio-button']//p[text()='Manual Payment']")))
        payment_option.click()

        continue_to_review_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Place the order
        place_order_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Confirm order success
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Your order was placed successfully')]")))
        self.assertTrue(success_message.is_displayed(), "Order success message not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()