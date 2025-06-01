from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open menu
        try:
            menu_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()
        except:
            self.fail("Menu button not found")

        # Go to store page
        try:
            store_link = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()
        except:
            self.fail("Store link not found")

        # Click on the first product
        try:
            first_product = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[data-testid='products-list'] > li:nth-child(1) > a"))
            )
            first_product.click()
        except:
            self.fail("First product link not found")

        # Select size
        try:
            size_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='product-options'] > button:nth-child(1)"))
            )
            size_button.click()
        except:
            self.fail("Size button not found")

        # Add to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found")

        # Go to cart
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:'] > a[data-testid='nav-cart-link']"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found")

        # Go to checkout
        try:
            go_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='nav-cart-dropdown'] > div > a > button[data-testid='go-to-cart-button']"))
            )
            go_to_cart_button.click()
        except:
            self.fail("Go to cart button not found")

        # Fill shipping address
        try:
            sign_in_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a > button[data-testid='sign-in-button']"))
            )
        except:
            pass

        try:
            shipping_first_name = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
            )
            shipping_first_name.send_keys("user")

            shipping_last_name = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']"))
            )
            shipping_last_name.send_keys("test")

            shipping_address = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']"))
            )
            shipping_address.send_keys("street 1")

            shipping_postal_code = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']"))
            )
            shipping_postal_code.send_keys("LV-1021")

            shipping_city = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']"))
            )
            shipping_city.send_keys("Riga")

            shipping_country = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']"))
            )
            shipping_country.send_keys("Denmark")

            shipping_email = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))
            )
            shipping_email.send_keys("user@test.com")

            submit_address_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']"))
            )
            submit_address_button.click()
        except:
            self.fail("Shipping address fields not found or submit failed")

        # Select delivery option
        try:
            delivery_option = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']:nth-child(1) > div > button[data-testid='radio-button']"))
            )
            delivery_option.click()

            submit_delivery_option_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']"))
            )
            submit_delivery_option_button.click()
        except:
            self.fail("Delivery option not found or submit failed")

        # Select payment option
        try:
            payment_option = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='headlessui-radiogroup-:rj:'] > div > span[id='headlessui-radio-:rk:'] > div > div > button[data-testid='radio-button']"))
            )
            payment_option.click()

            submit_payment_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']"))
            )
            submit_payment_button.click()
        except:
            self.fail("Payment option not found or submit failed")

        # Place order
        try:
            submit_order_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))
            )
            submit_order_button.click()
        except:
            self.fail("Submit order button not found")

        # Verify success message
        try:
            success_message = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='order-complete-container'] > h1 > span:nth-child(2)"))
            )
            self.assertEqual(success_message.text, "Your order was placed successfully.")
        except:
            self.fail("Success message not found or incorrect")

if __name__ == "__main__":
    unittest.main()