from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Click on the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Click on a product image (thumbnail)
        product_thumbnail = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a")))
        product_thumbnail.click()

        # Select a size
        size_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']")))
        size_option.click()

        # Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout fields
        self.fill_checkout_fields(wait)

        # Select delivery method
        delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button")))
        delivery_option.click()

        # Select payment method
        payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#headlessui-radio-:rk: button")))
        payment_option.click()

        # Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify confirmation
        confirmation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Your order was placed successfully')]")))
        self.assertIn("Your order was placed successfully", confirmation_text.text)

    def fill_checkout_fields(self, wait):
        # Fill required fields
        first_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")))
        first_name.send_keys("user")

        last_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")))
        last_name.send_keys("test")

        address = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")))
        address.send_keys("street 1")

        postal_code = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")))
        postal_code.send_keys("LV-1021")

        city = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")))
        city.send_keys("Riga")

        country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
        country_select.send_keys("Denmark")

        email = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")))
        email.send_keys("user@test.com")

        # Continue to delivery
        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        continue_button.click()

if __name__ == "__main__":
    unittest.main()