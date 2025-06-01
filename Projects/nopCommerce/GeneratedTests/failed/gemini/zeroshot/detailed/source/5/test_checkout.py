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
from selenium.webdriver.support.ui import Select


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
        self.random_email = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + "@test.com"

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        search_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_input.send_keys("book")

        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
        )
        search_button.click()

        # 3. Add the first result to the cart using a product tile button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # 4. From the success notification, click the "shopping cart" link.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
        )
        shopping_cart_link.click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_of_service_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "termsofservice"))
        )
        terms_of_service_checkbox.click()

        checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # 7. Fill out the full billing form (from credentials).
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
        )
        first_name_input.send_keys(self.credentials["FirstName"])

        last_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
        )
        last_name_input.send_keys(self.credentials["LastName"])

        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
        )
        email_input.send_keys(self.random_email)

        country_select = Select(WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
        ))
        country_select.select_by_value(self.credentials["CountryId"])

        state_province_select = Select(WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
        ))
        state_province_select.select_by_value(self.credentials["StateProvinceId"])

        city_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
        )
        city_input.send_keys(self.credentials["City"])

        address1_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
        )
        address1_input.send_keys(self.credentials["Address1"])

        zip_postal_code_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
        )
        zip_postal_code_input.send_keys(self.credentials["ZipPostalCode"])

        phone_number_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
        )
        phone_number_input.send_keys(self.credentials["PhoneNumber"])

        billing_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
        )
        billing_continue_button.click()

        # 8. Proceed through the following:
        #    - Shipping method step.
        shipping_method_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["ShippingOption"]))
        )
        shipping_method_option.click()

        shipping_method_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
        )
        shipping_method_continue_button.click()

        #    - Payment method step.
        payment_method_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["PaymentMethodOption"]))
        )
        payment_method_option.click()

        payment_method_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
        )
        payment_method_continue_button.click()

        #    - Payment info step (fill in credit card details from credentials if necessary).
        credit_card_type_select = Select(WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CreditCardType"))
        ))
        credit_card_type_select.select_by_value(self.credentials["CreditCardType"])

        cardholder_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardholderName"))
        )
        cardholder