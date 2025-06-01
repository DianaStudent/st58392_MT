```python
import unittest
import random
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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver: WebDriver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()
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
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")

        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # 3. Add the first result to the cart using a product tile button.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. From the success notification, click the "shopping cart" link.
        shopping_cart_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='bar-notification success']/p[@class='content']/a[contains(text(), 'shopping cart')]")))
        shopping_cart_link.click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_of_service_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()

        checkout_button = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill out the full billing form (from credentials):
        #    - First name, last name, email (generated), address, city, country, zip code, phone.
        #    - Use select tags for country and state/province if available.
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        first_name_input.send_keys(self.credentials["FirstName"])

        last_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName")))
        last_name_input.send_keys(self.credentials["LastName"])

        email_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Email")))
        email_input.send_keys(self.email)

        country_select = Select(wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))))
        country_select.select_by_value(self.credentials["CountryId"])

        city_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_City")))
        city_input.send_keys(self.credentials["City"])

        address1_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1")))
        address1_input.send_keys(self.credentials["Address1"])

        zip_postal_code_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode")))
        zip_postal_code_input.send_keys(self.credentials["ZipPostalCode"])

        phone_number_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber")))
        phone_number_input.send_keys(self.credentials["PhoneNumber"])

        billing_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-address-next-step-button")))
        billing_continue_button.click()

        # 8. Proceed through the following:
        #    - Shipping method step.
        shipping_method_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.credentials["ShippingOption"])))
        shipping_method_option.click()

        shipping_method_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shipping-method-next-step-button")))
        shipping_method_continue_button.click()

        #    - Payment method step.
        payment_method_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.credentials["PaymentMethodOption"])))
        payment_method_option.click()

        payment_method_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-method-next-step-button")))
        payment_method_continue_button.click()

        #    - Payment info step (fill in credit card details from credentials if necessary).
        credit_card_type_select = Select(wait.until(EC.presence_of_element_located((By.ID, "CreditCardType"))))
        credit_card_type_select.select_by_value(self.credentials["CreditCardType"])

        cardholder_name_input = wait.until(EC.presence_of_element_located((By.ID, "CardholderName")))
        cardholder_name_input.send_keys(self.credentials["CardholderName"])

        card_number_input = wait.until(EC.presence_of_element_located((By.ID, "CardNumber")))
        card_number_input.send_keys(self.credentials["CardNumber"])

        expire_month_select = Select(wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth"))))
        expire_month_select.select_by_value(self.credentials["ExpireMonth"])

        expire_year_select = Select(wait.until(EC.presence_of_element_located((By.ID, "ExpireYear"))))
        expire_year_select.select_by_value(self.credentials["ExpireYear"])

        card_code_input = wait.until(EC.presence_of_element_located((By.ID, "CardCode")))
        card_code_input.send_keys(self.credentials["CardCode"])

        payment_info_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-info-next-step-button")))
        payment_info_continue_button.click()

        # 9.