from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.ID, "headlessui-popover-button-:R6qdtt7:")))
        menu_button.click()

        # Step 2: Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on a product image - first product
        product_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt'] img")))
        product_image.click()

        # Step 4 & 5: Select size and add to cart
        size_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']")))
        size_button.click()

        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Step 6: Click the cart button
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7: Click "Go to checkout"
        go_to_checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout.click()

        # Step 8: Fill checkout fields
        self.fill_checkout_fields()

        # Step 9: Continue to delivery
        continue_to_delivery_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

        # Step 10: Select delivery method
        delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']")))
        delivery_option.click()

        continue_to_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        # Step 11: Select payment method
        payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id*='headlessui-radio'] button")))
        payment_option.click()

        continue_to_review_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        continue_to_review_button.click()

        # Step 12: Place the order
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 13: Verify the confirmation
        confirmation_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='order-complete-container'] h1")))
        self.assertIn("Your order was placed successfully", confirmation_message.text)

    def fill_checkout_fields(self):
        driver = self.driver

        # Fill out checkout form
        first_name = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")
        last_name = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")
        address = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")
        postal_code = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")
        city = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")
        country = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
        email = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")

        first_name.send_keys("user")
        last_name.send_keys("test")
        address.send_keys("street 1")
        postal_code.send_keys("LV-1021")
        city.send_keys("Riga")
        email.send_keys("user@test.com")
        country.send_keys("Denmark")
        country.send_keys(Keys.RETURN)

if __name__ == "__main__":
    unittest.main()