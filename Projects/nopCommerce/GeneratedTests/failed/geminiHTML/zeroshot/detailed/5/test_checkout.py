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
import random

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_url = "http://max/"
        self.email = f"user_{''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(8))}@test.com"
        self.credentials = {
            "FirstName": "Test",
            "LastName": "User",
            "Email": self.email,
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

        # 1. Navigate to the "Search" page and look for a product using the query "book".
        search_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_input.send_keys("book")

        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-button"))
        )
        search_button.click()

        # 3. Add the first result to the cart using a product tile button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # 4. From the success notification, click the "shopping cart" link.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='bar-notification success']/p[@class='content']/a[text()='shopping cart']"))
        )
        shopping_cart_link.click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        try:
            terms_of_service_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "termsofservice"))
            )
            terms_of_service_checkbox.click()
        except:
            self.fail("Terms of service checkbox not found")

        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Checkout button not found")

        # 6. Choose "Checkout as Guest".
        try:
            checkout_as_guest_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            checkout_as_guest_button.click()
        except:
            self.fail("Checkout as Guest button not found")

        # 7. Fill out the full billing form (from credentials).
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
        )

        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys(self.credentials["FirstName"])
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys(self.credentials["LastName"])
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys(self.credentials["Email"])
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys(self.credentials["City"])
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys(self.credentials["Address1"])
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys(self.credentials["ZipPostalCode"])
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys(self.credentials["PhoneNumber"])

        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_select.click()
        country_select.send_keys(self.credentials["CountryId"])

        state_province_select = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        state_province_select.click()
        state_province_select.send_keys(self.credentials["StateProvinceId"])

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
        )
        continue_button.click()

        # 8. Proceed through the following steps:
        # Shipping method step.
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "shipping-method-buttons-container"))
        )
        shipping_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["ShippingOption"]))
        )
        shipping_option.click()

        shipping_method_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
        )
        shipping_method_continue_button.click()

        # Payment method step.
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "payment-method-buttons-container"))
        )

        payment_method_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["PaymentMethodOption"]))
        )
        payment_method_option.click()

        payment_method_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
        )
        payment_method_continue_button.click()

        # Payment info step (fill in credit card details from credentials if necessary).
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "payment-info-buttons-container"))
        )

        cardholder_name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardholderName"))
        )
        cardholder_name.send_keys(self.credentials["CardholderName"])

        card_number = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardNumber"))
        )
        card_number.send_keys(self.credentials["CardNumber"])

        expire_month = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ExpireMonth"))
        )
        expire_month.click()
        expire_month.send_keys(self.credentials