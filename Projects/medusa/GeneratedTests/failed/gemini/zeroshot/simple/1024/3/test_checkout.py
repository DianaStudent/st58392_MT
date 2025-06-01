from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        # Go to store page
        try:
            menu_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()
        except:
            self.fail("Could not find menu button")

        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()
        except:
            self.fail("Could not find store link")

        # Go to product page
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
            )
            product_link.click()
        except:
            self.fail("Could not find product link")

       # Select size
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']"))
            )
            size_button.click()
        except:
            self.fail("Could not find size button")

        # Add to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find add to cart button")

        # Go to cart
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']"))
            )
            cart_button.click()
        except:
            self.fail("Could not find cart button")

        # Go to checkout
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] > button[data-testid='go-to-cart-button']"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Could not find go to checkout button")

        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] > button"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Could not find go to checkout button")

        # Fill shipping address
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
            )
            first_name_input.send_keys("user")
        except:
            self.fail("Could not find first name input")

        try:
            last_name_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']"))
            )
            last_name_input.send_keys("test")
        except:
            self.fail("Could not find last name input")

        try:
            address_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']"))
            )
            address_input.send_keys("street 1")
        except:
            self.fail("Could not find address input")

        try:
            postal_code_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']"))
            )
            postal_code_input.send_keys("LV-1021")
        except:
            self.fail("Could not find postal code input")

        try:
            city_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']"))
            )
            city_input.send_keys("Riga")
        except:
            self.fail("Could not find city input")

        try:
            country_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']"))
            )
            select = Select(country_select)
            select.select_by_value("dk")
        except:
            self.fail("Could not find country select")

        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))
            )
            email_input.send_keys("user@test.com")
        except:
            self.fail("Could not find email input")

        try:
            submit_address_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']"))
            )
            submit_address_button.click()
        except:
            self.fail("Could not find submit address button")

        # Select delivery option
        try:
            delivery_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']:nth-child(1) > div > button[data-testid='radio-button']"))
            )
            delivery_option.click()
        except:
            self.fail("Could not find delivery option")

        try:
            submit_delivery_option_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']"))
            )
            submit_delivery_option_button.click()
        except:
            self.fail("Could not find submit delivery option button")

        # Select payment option
        try:
            payment_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='headlessui-radiogroup-:rj:'] > div > span[id='headlessui-radio-:rk:'] > div > button[data-testid='radio-button']"))
            )
            payment_option.click()
        except:
            self.fail("Could not find payment option")

        try:
            submit_payment_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']"))
            )
            submit_payment_button.click()
        except:
            self.fail("Could not find submit payment button")

        # Place order
        try:
            submit_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='