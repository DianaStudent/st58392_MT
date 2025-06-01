```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Open menu
        try:
            menu_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()
        except Exception as e:
            self.fail(f"Could not find or click menu button: {e}")

        # Go to store
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()
        except Exception as e:
            self.fail(f"Could not find or click store link: {e}")

        # Click on product
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
            )
            product_link.click()
        except Exception as e:
            self.fail(f"Could not find or click product link: {e}")

        # Select size
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button'][text()='L']"))
            )
            size_button.click()
        except Exception as e:
            self.fail(f"Could not find or click size button: {e}")

        # Add to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click add to cart button: {e}")

        # Go to cart
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click cart button: {e}")

        # Go to checkout
        try:
            go_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] > button[data-testid='go-to-cart-button']"))
            )
            go_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click go to checkout button: {e}")

        # Fill shipping address
        try:
            shipping_first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
            )
            shipping_first_name_input.clear()
            shipping_first_name_input.send_keys("user")

            shipping_last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']"))
            )
            shipping_last_name_input.clear()
            shipping_last_name_input.send_keys("test")

            shipping_address_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']"))
            )
            shipping_address_input.clear()
            shipping_address_input.send_keys("street 1")

            shipping_postal_code_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']"))
            )
            shipping_postal_code_input.clear()
            shipping_postal_code_input.send_keys("LV-1021")

            shipping_city_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']"))
            )
            shipping_city_input.clear()
            shipping_city_input.send_keys("Riga")

            shipping_country_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']"))
            )
            shipping_country_select.click()
            shipping_country_select.send_keys("Denmark")

            shipping_email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))
            )
            shipping_email_input.clear()
            shipping_email_input.send_keys("user@test.com")
        except Exception as e:
            self.fail(f"Could not fill shipping address: {e}")

        # Submit shipping address
        try:
            submit_address_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']"))
            )
            submit_address_button.click()
        except Exception as e:
            self.fail(f"Could not submit shipping address: {e}")

        # Select delivery option
        try:
            delivery_option_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']:first-child button[data-testid='radio-button']"))
            )
            delivery_option_radio.click()
        except Exception as e:
            self.fail(f"Could not select delivery option: {e}")

        # Submit delivery option
        try:
            submit_delivery_option_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']"))
            )
            submit_delivery_option_button.click()
        except Exception as e:
            self.fail(f"Could not submit delivery option: {e}")

        # Select payment method
        try:
            payment_method_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:'] button[data-testid='radio-button']"))
            )
            payment_method_radio.click()
        except Exception as e:
            self.fail(f"Could not select payment method: {e}")

        # Submit payment
        try:
            submit_payment_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']"))
            )
            submit_payment_button.click()
        except Exception as e:
            self.fail(f"Could not submit payment: {e}")

        # Place order
        try:
            submit_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR