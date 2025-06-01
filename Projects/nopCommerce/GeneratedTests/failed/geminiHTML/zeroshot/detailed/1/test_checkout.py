from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```python
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import uuid

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_url = "http://max/"
        self.email = f"user_{uuid.uuid4().hex}@test.com"
        self.credentials = {
            "FirstName": "Test",
            "LastName": "User",
            "Email": self.email,
            "City": "Riga",
            "Address1": "Street 1",
            "ZipPostalCode": "LV-1234",
            "PhoneNumber": "12345678",
            "CountryId": "237", #United States of America
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

        # 1. Navigate to the "Search" page and look for a product using the query "book".
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click Search link: {e}")

        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_input.send_keys("book")
            search_button.click()
        except Exception as e:
            self.fail(f"Failed to interact with search input or button: {e}")

        # 3. Add the first result to the cart using a product tile button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click add to cart button: {e}")

        # 4. From the success notification, click the "shopping cart" link.
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click shopping cart link in notification: {e}")

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        try:
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "termsofservice"))
            )
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout"))
            )
            terms_checkbox.click()
            checkout_button.click()
        except Exception as e:
            self.fail(f"Failed to interact with terms checkbox or checkout button: {e}")

        # 6. Choose "Checkout as Guest".
        try:
            guest_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            guest_checkout_button.click()
        except Exception as e:
            self.fail(f"Failed to click checkout as guest button: {e}")

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
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
            )
            city_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            address1_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            zip_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            phone_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )

            first_name_input.send_keys(self.credentials["FirstName"])
            last_name_input.send_keys(self.credentials["LastName"])
            email_input.send_keys(self.credentials["Email"])
            city_input.send_keys(self.credentials["City"])
            address1_input.send_keys(self.credentials["Address1"])
            zip_input.send_keys(self.credentials["ZipPostalCode"])
            phone_input.send_keys(self.credentials["PhoneNumber"])

            # Select country and state
            for element_id, value in [("BillingNewAddress_CountryId", self.credentials["CountryId"]), ("BillingNewAddress_StateProvinceId", self.credentials["StateProvinceId"])]:
                element = driver.find_element(By.ID, element_id)
                for option in element.find_elements(By.TAG_NAME, 'option'):
                    if option.get_attribute('value') == value:
                        option.click()
                        break

        except Exception as e:
            self.fail(f"Failed to fill billing form: {e}")

        # 8. Proceed through the following steps.
        try:
            billing_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            billing_continue_button.click()
        except Exception as e:
            self.fail(f"Failed to click billing continue button: {e}")

        # Shipping method step.
        try:
            shipping_method_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["ShippingOption"]))
            )
            shipping_method_option.click()
            shipping_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_continue_button.click()
        except Exception as e:
            self.fail(f"Failed to select shipping method or click continue: {e}")

        # Payment method