from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```python
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import uuid

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

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click search link: {e}")

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

        # 3. Add the first result to the cart using a product tile button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add product to cart: {e}")

        # 4. From the success notification, click the "shopping cart" link.
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Failed to click shopping cart link: {e}")

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
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
            self.fail(f"Failed to accept terms or click checkout: {e}")

        # 6. Choose "Checkout as Guest".
        try:
            checkout_as_guest_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            checkout_as_guest_button.click()
        except Exception as e:
            self.fail(f"Failed to checkout as guest: {e}")

        # 7. Fill out the full billing form (from credentials).
        try:
            email = f"user_{uuid.uuid4().hex}@test.com"
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName"))).send_keys(self.credentials["FirstName"])
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_LastName"))).send_keys(self.credentials["LastName"])
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_Email"))).send_keys(email)
            country_select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
            country_select.send_keys(Keys.CONTROL + "a")
            country_select.send_keys(Keys.DELETE)
            country_select.send_keys(self.credentials["CountryId"])
            state_select = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
            state_select.send_keys(Keys.CONTROL + "a")
            state_select.send_keys(Keys.DELETE)
            state_select.send_keys(self.credentials["StateProvinceId"])
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_City"))).send_keys(self.credentials["City"])
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_Address1"))).send_keys(self.credentials["Address1"])
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_ZipPostalCode"))).send_keys(self.credentials["ZipPostalCode"])
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_PhoneNumber"))).send_keys(self.credentials["PhoneNumber"])

            continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            continue_button.click()
        except Exception as e:
            self.fail(f"Failed to fill billing form: {e}")

        # 8. Proceed through the following steps.
        # Shipping method step.
        try:
            shipping_method = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["ShippingOption"]))
            )
            shipping_method.click()
            shipping_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_continue_button.click()
        except Exception as e:
            self.fail(f"Failed to select shipping method: {e}")

        # Payment method step.
        try:
            payment_method = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["PaymentMethodOption"]))
            )
            payment_method.click()
            payment_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            payment_continue_button.click()
        except Exception as e:
            self.fail(f"Failed to select payment method: {e}")

        # Payment info step (fill in credit card details from credentials if necessary).
        try:
            card_type_select = WebDriverWait(driver, 20).until(EC.presence_of_