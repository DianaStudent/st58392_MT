from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Open home page and click on the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-menu-button']")))
        menu_button.click()

        # Click the "Store" link in the menu
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='store-link']")))
        store_link.click()

        # Click on a product image (thumbnail)
        product_thumbnail = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a")))
        product_thumbnail.click()

        # Select a size
        size_button = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='option-button']")))[0]
        size_button.click()

        # Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        cart_button.click()

        # Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill in checkout fields
        self.fill_checkout_fields()

        # Select delivery and payment methods
        delivery_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='delivery-option-radio'] button"))).click()
        continue_to_payment_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='submit-delivery-option-button']"))).click()
        
        payment_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='radio-button']"))).click()
        continue_to_review_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='submit-payment-button']"))).click()

        # Click "Place Order"
        place_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='submit-order-button']")))
        place_order_button.click()
        
        # Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='order-complete-container'] h1 > span:last-child")))
        
        if not confirmation_text or "Your order was placed successfully" not in confirmation_text.text:
            self.fail("Order confirmation message is not as expected.")

    def fill_checkout_fields(self):
        driver = self.driver
        wait = self.wait

        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='shipping-first-name-input']")))
        last_name_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-last-name-input']")
        address_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-address-input']")
        postal_code_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-postal-code-input']")
        city_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-city-input']")
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-email-input']")
        country_select = driver.find_element(By.CSS_SELECTOR, "[data-testid='shipping-country-select']")

        first_name_input.clear()
        last_name_input.clear()
        address_input.clear()
        postal_code_input.clear()
        city_input.clear()
        email_input.clear()

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        address_input.send_keys("street 1")
        postal_code_input.send_keys("LV-1021")
        city_input.send_keys("Riga")
        email_input.send_keys("user@test.com")
        country_select.click()
        
        country_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[value='dk']")))
        country_option.click()

        continue_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='submit-address-button']")
        continue_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()