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

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        search_link_locator = (By.LINK_TEXT, "Search")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_link_locator)).click()
        search_input_locator = (By.ID, "q")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_input_locator)).send_keys("book")
        search_button_locator = (By.CLASS_NAME, "search-button")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(search_button_locator)).click()

        # 3. Add the first result to the cart using a product tile button.
        add_to_cart_button_locator = (By.CLASS_NAME, "product-box-add-to-cart-button")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(add_to_cart_button_locator)).click()

        # 4. From the success notification, click the "shopping cart" link.
        shopping_cart_link_locator = (By.LINK_TEXT, "shopping cart")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(shopping_cart_link_locator)).click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_of_service_checkbox_locator = (By.ID, "termsofservice")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(terms_of_service_checkbox_locator)).click()
        checkout_button_locator = (By.ID, "checkout")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(checkout_button_locator)).click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button_locator = (By.CLASS_NAME, "checkout-as-guest-button")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(checkout_as_guest_button_locator)).click()

        # 7. Fill out the full billing form
        billing_form_locator = (By.ID, "co-billing-form")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(billing_form_locator))

        first_name_locator = (By.ID, "BillingNewAddress_FirstName")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(first_name_locator)).send_keys(self.credentials["FirstName"])

        last_name_locator = (By.ID, "BillingNewAddress_LastName")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(last_name_locator)).send_keys(self.credentials["LastName"])

        email_locator = (By.ID, "BillingNewAddress_Email")
        random_email = f"user_{uuid.uuid4().hex[:8]}@test.com"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(email_locator)).send_keys(random_email)

        country_locator = (By.ID, "BillingNewAddress_CountryId")
        country_select = Select(WebDriverWait(driver, 20).until(EC.presence_of_element_located(country_locator)))
        country_select.select_by_value(self.credentials["CountryId"])

        state_locator = (By.ID, "BillingNewAddress_StateProvinceId")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(state_locator))
        state_select = Select(driver.find_element(*state_locator))
        state_select.select_by_value(self.credentials["StateProvinceId"])

        city_locator = (By.ID, "BillingNewAddress_City")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(city_locator)).send_keys(self.credentials["City"])

        address1_locator = (By.ID, "BillingNewAddress_Address1")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(address1_locator)).send_keys(self.credentials["Address1"])

        zip_locator = (By.ID, "BillingNewAddress_ZipPostalCode")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(zip_locator)).send_keys(self.credentials["ZipPostalCode"])

        phone_locator = (By.ID, "BillingNewAddress_PhoneNumber")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(phone_locator)).send_keys(self.credentials["PhoneNumber"])

        billing_continue_button_locator = (By.CLASS_NAME, "new-address-next-step-button")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(billing_continue_button_locator)).click()

        # 8. Proceed through the following steps
        # Shipping method step.
        shipping_method_locator = (By.CSS_SELECTOR, self.credentials["ShippingOption"])
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(shipping_method_locator)).click()
        shipping_continue_button_locator = (By.CLASS_NAME, "shipping-method-next-step-button")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(shipping_continue_button_locator)).click()

        # Payment method step.
        payment_method_locator = (By.CSS_SELECTOR, self.credentials["PaymentMethodOption"])
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(payment_method_locator)).click()
        payment_continue_button_locator = (By.CLASS_NAME, "payment-method-next-step-button")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(payment_continue_button_locator)).click()

        # Payment info step
        credit_card_type_locator = (By.ID, "CreditCardType")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(credit_card_type_locator))
        credit_card_type_select = Select(driver.find_element(*credit_card_type_locator))
        credit_card_type_select.select_by_value(self.credentials["CreditCardType"])

        cardholder_name_locator = (By.ID, "CardholderName")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(cardholder_name_locator)).send_keys(self.credentials["CardholderName"])

        card_number