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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.credentials = {
            "FirstName": "Test",
            "LastName": "User",
            "Email": "random_email",
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
        # 1. Open the home page.
        self.assertEqual(driver.current_url, "http://max/")

        # 2. Click on the "Search" link and search for a product (e.g. "book").
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

        # 3. Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # 4. Open the shopping cart via the success notification popup.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
        )
        shopping_cart_link.click()

        # 5. Accept terms of service and click the "Checkout" button.
        terms_of_service_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "termsofservice"))
        )
        terms_of_service_checkbox.click()

        checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # 7. Fill in the billing address.
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
        email_input.send_keys(self.credentials["Email"] + "@test.com")

        country_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
        )
        country_select = Select(country_select)
        country_select.select_by_value(self.credentials["CountryId"])

        state_province_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
        )
        state_province_select = Select(state_province_select)
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

        # 8. Select shipping and payment methods.
        shipping_method_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["ShippingOption"]))
        )
        shipping_method_option.click()

        shipping_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
        )
        shipping_continue_button.click()

        payment_method_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["PaymentMethodOption"]))
        )
        payment_method_option.click()

        payment_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
        )
        payment_continue_button.click()

        # 9. Enter credit card details.
        credit_card_type_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CreditCardType"))
        )
        credit_card_type_select = Select(credit_card_type_select)
        credit_card_type_select.select_by_value(self.credentials["CreditCardType"])

        cardholder_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardholderName"))
        )
        cardholder_name_input.send_keys(self.credentials["CardholderName"])

        card_number_input = WebDriverWait(driver, 20).until(