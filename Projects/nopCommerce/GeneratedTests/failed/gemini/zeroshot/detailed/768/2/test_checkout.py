from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```python
import unittest
import time
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://max/"
        self.credentials = {
            "FirstName": "Test",
            "LastName": "User",
            "City": "Riga",
            "Address1": "Street 1",
            "ZipPostalCode": "LV-1234",
            "PhoneNumber": "12345678",
            "CountryId": "124",
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

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Navigate to the "Search" page
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click Search link: {e}")

        # 2. Search for a product
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Failed to search for product: {e}")

        # 3. Add the first result to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add product to cart: {e}")

        # 4. Click the "shopping cart" link from the success notification
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Failed to click shopping cart link: {e}")

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button
        try:
            terms_of_service_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "termsofservice"))
            )
            terms_of_service_checkbox.click()
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Failed to accept terms and checkout: {e}")

        # 6. Choose "Checkout as Guest"
        try:
            checkout_as_guest_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            checkout_as_guest_button.click()
        except Exception as e:
            self.fail(f"Failed to checkout as guest: {e}")

        # 7. Fill out the billing form
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            first_name_input.send_keys(self.credentials["FirstName"])

            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            last_name_input.send_keys(self.credentials["LastName"])

            email = f"user_{uuid.uuid4().hex}@test.com"
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            email_input.send_keys(email)

            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            country_select_element = Select(country_select)
            country_select_element.select_by_value(self.credentials["CountryId"])

            state_province_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
            )
            state_province_select_element = Select(state_province_select)
            state_province_select_element.select_by_value(self.credentials["StateProvinceId"])


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

        except Exception as e:
            self.fail(f"Failed to fill out billing form: {e}")

        # 8. Proceed through Shipping method step
        try:
            shipping_method_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["ShippingOption"]))
            )
            shipping_method_option.click()

            shipping_method_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_method_continue_button.click()
        except Exception as e:
            self.fail(f"Failed to select shipping method and continue: {e}")

        # 9. Proceed through Payment method step
        try:
            payment_method_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["PaymentMethodOption"]))
            )
            payment_method_option.click()
            payment_method_continue_button = WebDriverWait(