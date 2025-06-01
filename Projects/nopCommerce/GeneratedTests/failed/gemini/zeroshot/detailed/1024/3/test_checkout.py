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

    def tearDown(self):
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
            EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[contains(@href, '/cart')]"))
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

        # 7. Fill out the full billing form.
        email = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + "@test.com"
        self.credentials["Email"] = email
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
        )

        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys(self.credentials["FirstName"])
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys(self.credentials["LastName"])
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys(self.credentials["Email"])
        
        country_select = Select(driver.find_element(By.ID, "BillingNewAddress_CountryId"))
        country_select.select_by_value(self.credentials["CountryId"])
        
        state_province_select = Select(driver.find_element(By.ID, "BillingNewAddress_StateProvinceId"))
        state_province_select.select_by_value(self.credentials["StateProvinceId"])

        driver.find_element(By.ID, "BillingNewAddress_City").send_keys(self.credentials["City"])
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys(self.credentials["Address1"])
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys(self.credentials["ZipPostalCode"])
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys(self.credentials["PhoneNumber"])

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
        )
        continue_button.click()

        # 8. Proceed through the following steps:
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

        #    - Payment info step.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardholderName"))
        )

        card_type_select = Select(driver.find_element(By.ID, "CreditCardType"))
        card_type_select.select_by_value(self.credentials["CreditCardType"])
        driver.find_element(By.ID, "CardholderName").send_keys(self.credentials["CardholderName"])
        driver.find_element(By.ID, "CardNumber").send_keys(self.credentials["CardNumber"])
        
        expire_month_select = Select(driver.find_element(By.ID, "ExpireMonth"))
        expire_month_select.select_by_value(self.credentials["ExpireMonth"])
        
        expire_year_select = Select(driver.find_element(By.ID, "ExpireYear"))
        expire_year_select.select_by_value(self.credentials["ExpireYear"])
        
        driver.find_element(By.ID, "CardCode").send_keys(self.credentials["CardCode"])

        payment_info_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button"))
        )
        payment_info_continue_button.click()

        # 9. On the confirm step, click “Confirm” and wait for the success message.
        confirm_order_button = WebDriverWait(