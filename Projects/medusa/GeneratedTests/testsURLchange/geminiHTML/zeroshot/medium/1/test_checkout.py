```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


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

        # 1. Open home page.
        self.assertEqual(driver.current_url, "http://localhost:8000/dk/")

        # 2. Click on the menu button.
        try:
            menu_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()
        except Exception as e:
            self.fail(f"Menu button not found or not clickable: {e}")

        # 3. Click on the "Store" link.
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()
        except Exception as e:
            self.fail(f"Store link not found or not clickable: {e}")

        # 4. Click on a product image (thumbnail).
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt'] div[data-testid='product-wrapper'] div img"))
            )
            product_link.click()
        except Exception as e:
            self.fail(f"Product link not found or not clickable: {e}")

        # 5. Select a size.
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']"))
            )
            size_button.click()
        except Exception as e:
            self.fail(f"Size button not found or not clickable: {e}")

        # 6. Click the "Add to Cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickable: {e}")

        # 7. Click the cart button to open the cart.
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:'] a[data-testid='nav-cart-link']"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found or not clickable: {e}")

        # 8. Click "Go to checkout", fill checkout fields:
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] button[data-testid='go-to-cart-button']"))
            )
            go_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Go to checkout button not found or not clickable: {e}")

        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout button not found or not clickable: {e}")

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
            )
            first_name_input.send_keys("user")

            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']"))
            )
            last_name_input.send_keys("test")

            address_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']"))
            )
            address_input.send_keys("street 1")

            postal_code_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']"))
            )
            postal_code_input.send_keys("LV-1021")

            city_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']"))
            )
            city_input.send_keys("Riga")

            country_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']"))
            )
            select = Select(country_select)
            select.select_by_value("dk")

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))
            )
            email_input.send_keys("user@test.com")

            submit_address_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']"))
            )
            submit_address_button.click()

        except Exception as e:
            self.fail(f"Checkout fields not found or not interactable: {e}")

        # 9. Select delivery and payment methods.
        try:
            delivery_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']"))
            )
            delivery_option.click()

            submit_delivery_option_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']"))
            )
            submit_delivery_option_button.click()

            payment_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:']"))
            )
            payment_option.click()

            submit_payment_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']"))
            )
            submit_payment_button.click()
        except Exception as e:
            self.fail(f"Delivery or payment options not found or not interactable: {e}")

        # 10. Click "Place Order".
        try:
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))
            )
            place_order_button.click()
        except Exception as e: