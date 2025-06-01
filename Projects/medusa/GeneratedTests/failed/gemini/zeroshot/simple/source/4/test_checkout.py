from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Go to store page by clicking on the store link in the nav bar
        store_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-store-link"]'))
        )
        store_link.click()

        # Click on the first product
        product_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/dk/products/sweatshirt"]'))
        )
        product_link.click()

        # Select size
        size_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="L"]'))
        )
        size_button.click()

        # Add to cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]'))
        )
        add_to_cart_button.click()

        # Go to cart
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]'))
        )
        cart_button.click()

        # Go to checkout
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-testid="checkout-button"] > button'))
        )
        go_to_checkout_button.click()

        # Fill shipping address form
        shipping_first_name_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-first-name-input"]'))
        )
        shipping_first_name_input.send_keys("user")

        shipping_last_name_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-last-name-input"]'))
        )
        shipping_last_name_input.send_keys("test")

        shipping_address_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-address-input"]'))
        )
        shipping_address_input.send_keys("street 1")

        shipping_postal_code_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-postal-code-input"]'))
        )
        shipping_postal_code_input.send_keys("LV-1021")

        shipping_city_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-city-input"]'))
        )
        shipping_city_input.send_keys("Riga")

        shipping_country_select = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[data-testid="shipping-country-select"]'))
        )
        shipping_country_select.send_keys("Denmark")

        shipping_email_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-testid="shipping-email-input"]'))
        )
        shipping_email_input.send_keys("user@test.com")

        submit_address_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-address-button"]'))
        )
        submit_address_button.click()

        # Select delivery option
        delivery_option_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(@data-testid, "delivery-option-radio")][1]//button[@data-testid="radio-button"]'))
        )
        delivery_option_button.click()

        submit_delivery_option_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-delivery-option-button"]'))
        )
        submit_delivery_option_button.click()

        # Select payment option
        payment_option_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(@id, "headlessui-radio")][1]//button[@data-testid="radio-button"]'))
        )
        payment_option_button.click()

        submit_payment_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-payment-button"]'))
        )
        submit_payment_button.click()

        # Place order
        submit_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="submit-order-button"]'))
        )
        submit_order_button.click()

        # Verify order success
        order_complete_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//h1/span[text()="Your order was placed successfully."]'))
        ).text
        self.assertIn("Your order was placed successfully", order_complete_text)

if __name__ == "__main__":
    unittest.main()