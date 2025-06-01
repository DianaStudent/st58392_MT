from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```python
import unittest
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class CheckoutTest(unittest.TestCase):
    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver: WebDriver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_url = "http://max/"
        self.credentials = {
            "FirstName": "Test",
            "LastName": "User",
            "City": "Riga",
            "Address1": "Street 1",
            "ZipPostalCode": "LV-1234",
            "PhoneNumber": "12345678",
            "CountryId": "237",
            "StateProvinceId": "0",
            "ShippingOption": "#shippingoption_1",
            "PaymentMethodOption": "#paymentmethod_1",
            "CreditCardType": "visa",
            "CardholderName": "Test User",
            "CardNumber": "4111111111111111",
            "ExpireMonth": "4",
            "ExpireYear": "2027",
            "CardCode": "123"
        }

    def tearDown(self):
        self.driver.quit()

    def generate_random_email(self):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(8))
        return f"user_{random_string}@test.com"

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except NoSuchElementException:
            self.fail("Search link not found")

        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_input.send_keys("book")
            search_button.click()
        except NoSuchElementException:
            self.fail("Search input or button not found")

        # 3. Add the first result to the cart using a product tile button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except NoSuchElementException:
            self.fail("Add to cart button not found")

        # 4. From the success notification, click the "shopping cart" link.
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
            )
            shopping_cart_link.click()
        except NoSuchElementException:
            self.fail("Shopping cart link not found in notification")

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        try:
            terms_of_service_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "termsofservice"))
            )
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout"))
            )

            terms_of_service_checkbox.click()
            checkout_button.click()
        except NoSuchElementException:
            self.fail("Terms of service checkbox or Checkout button not found")

        # 6. Choose "Checkout as Guest".
        try:
            checkout_as_guest_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            checkout_as_guest_button.click()
        except NoSuchElementException:
            self.fail("Checkout as Guest button not found")

        # 7. Fill out the full billing form.
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            state_province_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
            )
            city_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            address1_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            zip_postal_code_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            phone_number_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )

            first_name_input.send_keys(self.credentials["FirstName"])
            last_name_input.send_keys(self.credentials["LastName"])
            email_input.send_keys(self.generate_random_email())
            # country_select.send_keys(self.credentials["CountryId"])
            # state_province_select.send_keys(self.credentials["StateProvinceId"])
            city_input.send_keys(self.credentials["City"])
            address1_input.send_keys(self.credentials["Address1"])
            zip_postal_code_input.send_keys(self.credentials["ZipPostalCode"])
            phone_number_input.send_keys(self.credentials["PhoneNumber"])

            continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            continue_button.click()

        except NoSuchElementException:
            self.fail("Billing form element not found")

        # 8. Proceed through the following steps:
        #    - Shipping method step.
        try:
            shipping_method_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["ShippingOption"]))
            )
            shipping_method_option.click()
            shipping_method_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_method_continue_button.click()
        except NoSuchElementException:
            self.fail("Shipping method element not found")

        #    - Payment method step.
        try:
            payment_method_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["PaymentMethodOption"]))
            )
            payment_method_option.click()
            payment_method_continue_button = WebDriverWait(driver, 20).until(
                EC.presence_of_