from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class MedusaStoreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_checkout(self):
        driver = self.driver
        wait = self.wait
        
        # Open home page and click menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()
        
        # Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Click on the first product thumbnail
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a div img")))
        first_product.click()

        # Select size 'L'
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Add to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if not add_to_cart_button.is_enabled():
            self.fail("Add to cart button is not enabled")
        add_to_cart_button.click()

        # Open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout fields
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys('user')
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']"))).send_keys('test')
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']"))).send_keys('street 1')
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']"))).send_keys('LV-1021')
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']"))).send_keys('Riga')

        country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
        country_select.send_keys('Denmark')

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))).send_keys('user@test.com')

        # Continue to delivery
        continue_to_delivery_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
        continue_to_delivery_button.click()

        # Select delivery method
        delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='delivery-option-radio']")))
        delivery_option.click()
        
        # Continue to payment
        continue_to_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
        continue_to_payment_button.click()

        # Select payment method
        payment_method = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='headlessui-radiogroup-:rj:'] [data-testid='radio-button']")))
        payment_method.click()

        # Continue to review
        continue_to_review_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
        continue_to_review_button.click()

        # Place order
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify success message
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your order was placed successfully.']")))
        if not success_message or not success_message.is_displayed():
            self.fail("Success message not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()