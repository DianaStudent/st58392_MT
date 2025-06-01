```python
import unittest
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

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
        self.email = f"user_{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))}@test.com"

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # 1. Navigate to the "Search" page
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # 2. Search for a product
        search_input_id = "q"
        search_button_class = "button-1 search-button"

        search_input = self.wait.until(EC.presence_of_element_located((By.ID, search_input_id)))
        search_input.send_keys("book")
        search_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, search_button_class)))
        search_button.click()

        # 3. Add the first result to the cart
        add_to_cart_button_class = "button-2 product-box-add-to-cart-button"
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, add_to_cart_button_class)))
        add_to_cart_button.click()

        # 4. Click "shopping cart" from the success popup
        shopping_cart_link_text = "shopping cart"
        shopping_cart_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, shopping_cart_link_text)))
        shopping_cart_link.click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button
        terms_of_service_id = "termsofservice"
        checkout_button_class = "button-1 checkout-button"

        terms_of_service_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, terms_of_service_id)))
        terms_of_service_checkbox.click()

        checkout_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, checkout_button_class)))
        checkout_button.click()

        # 6. Choose "Checkout as Guest"
        checkout_as_guest_button_class = "button-1 checkout-as-guest-button"
        checkout_as_guest_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, checkout_as_guest_button_class)))
        checkout_as_guest_button.click()

        # 7. Fill out the billing form
        billing_form_fields = {
            "BillingNewAddress_FirstName": self.credentials["FirstName"],
            "BillingNewAddress_LastName": self.credentials["LastName"],
            "BillingNewAddress_Email": self.email,
            "BillingNewAddress_City": self.credentials["City"],
            "BillingNewAddress_Address1": self.credentials["Address1"],
            "BillingNewAddress_ZipPostalCode": self.credentials["ZipPostalCode"],
            "BillingNewAddress_PhoneNumber": self.credentials["PhoneNumber"]
        }

        for field_id, value in billing_form_fields.items():
            field = self.wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field.send_keys(value)

        country_select_id = "BillingNewAddress_CountryId"
        country_select = self.wait.until(EC.presence_of_element_located((By.ID, country_select_id)))
        country_select.send_keys("United States of America")

        state_select_id = "BillingNewAddress_StateProvinceId"
        state_select = self.wait.until(EC.presence_of_element_located((By.ID, state_select_id)))
        state_select.send_keys("Other")

        billing_continue_button_class = "button-1 new-address-next-step-button"
        billing_continue_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, billing_continue_button_class)))
        billing_continue_button.click()

        # 8. Proceed through the shipping method step
        shipping_method_option_id = "shippingoption_1"
        shipping_method_next_button_class = "button-1 shipping-method-next-step-button"

        shipping_method_option = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, shipping_method_option_id)))
        shipping_method_option.click()

        shipping_method_next_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, shipping_method_next_button_class)))
        shipping_method_next_button.click()

        # 9. Proceed through the payment method step
        payment_method_option_id = "paymentmethod_1"
        payment_method_next_button_class = "button-1 payment-method-next-step-button"

        payment_method_option = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, payment_method_option_id)))
        payment_method_option.click()

        payment_method_next_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, payment_method_next_button_class)))
        payment_method_next_button.click()

        # 10. Proceed through the payment info step
        payment_info_fields = {
            "CreditCardType": self.credentials["CreditCardType"],
            "CardholderName": self.credentials["CardholderName"],
            "CardNumber": self.credentials["CardNumber"],
            "ExpireMonth": self.credentials["ExpireMonth"],
            "ExpireYear": self.credentials["ExpireYear"],
            "CardCode": self.credentials["CardCode"]
        }

        for field_id, value in payment_info_fields.items():
            field = self.wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field.send_keys(value)

        payment_info_next_button_class = "button-1 payment-info-next-step-button"
        payment_info_next_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, payment_info_next_button_class)))
        payment_info_next_button.click()

        # 11. Confirm the order
        confirm_order_button_class = "button-1 confirm-order-next-step-button"
        confirm_order_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, confirm_order_button_class)))
        confirm_order_button.click()

        # 12. Verify order completion
        thank_you_header_xpath = "//h1[text()='Thank you']"
        try: