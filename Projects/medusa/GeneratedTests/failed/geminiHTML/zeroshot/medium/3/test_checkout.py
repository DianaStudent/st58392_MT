from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
from selenium.common.exceptions import NoSuchElementException

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

        # 1. Open home page (already done in setUp)

        # 2. Click on the menu button.
        try:
            menu_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()
        except NoSuchElementException:
            self.fail("Menu button not found")

        # 3. Click on the "Store" link.
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()
        except NoSuchElementException:
            self.fail("Store link not found")

        # 4. Click on a product image (thumbnail).
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
            )
            product_link.click()
        except NoSuchElementException:
            self.fail("Product link not found")

        # 5. Select a size.
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']"))
            )
            size_button.click()
        except NoSuchElementException:
            self.fail("Size button not found")

        # 6. Click the "Add to Cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except NoSuchElementException:
            self.fail("Add to cart button not found")

        # 7. Click the cart button to open the cart.
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']"))
            )
            cart_button.click()
        except NoSuchElementException:
            self.fail("Cart button not found")

        # 8. Click "Go to checkout", fill checkout fields
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] button[data-testid='go-to-cart-button']"))
            )
            go_to_checkout_button.click()
        except NoSuchElementException:
            self.fail("Go to checkout button not found")

        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/account'] button[data-testid='sign-in-button']"))
            )
        except NoSuchElementException:
            self.fail("Sign in button not found")

        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
            )
            first_name_input.send_keys("user")

            last_name_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']"))
            )
            last_name_input.send_keys("test")

            address_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']"))
            )
            address_input.send_keys("street 1")

            postal_code_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']"))
            )
            postal_code_input.send_keys("LV-1021")

            city_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']"))
            )
            city_input.send_keys("Riga")

            country_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']"))
            )
            country_select.click()
            country_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select'] option[value='dk']"))
            )
            country_option.click()

            email_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))
            )
            email_input.send_keys("user@test.com")

            submit_address_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']"))
            )
            submit_address_button.click()

        except NoSuchElementException:
            self.fail("Checkout field not found")

        # 9. Select delivery and payment methods.
        try:
            express_shipping_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button[data-testid='radio-button']"))
            )
            express_shipping_button.click()

            submit_delivery_option_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']"))
            )
            submit_delivery_option_button.click()

            manual_payment_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='headlessui-radiogroup-:rj:'] span[id='headlessui-radio-:rk:'] button[data-testid='radio-button']"))
            )
            manual_payment_button.click()

            submit_payment_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']"))
            )
            submit_payment_button.click()

        except NoSuchElementException:
            self.fail("Delivery or payment option not found")

        # 10. Click "Place Order".
        try:
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))
            )
            place_order_button.click()
        except NoSuchElementException:
            self.fail("Place order button not found")

        # 11. Verify the confirmation page contains: "Your order was placed successfully"
        try:
            confirmation_text