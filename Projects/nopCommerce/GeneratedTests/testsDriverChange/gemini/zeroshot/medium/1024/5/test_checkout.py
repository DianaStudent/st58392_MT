```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        try:
            home_page_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Your store name']")))
            self.assertIsNotNone(home_page_title)
        except NoSuchElementException:
            self.fail("Home page title is missing.")

        # 2. Click on the "Search" link and search for a product (e.g. "book").
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = wait.until(EC.visibility_of_element_located((By.ID, "q")))
        search_input.send_keys("book")

        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-button")))
        search_button.click()

        # 3. Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. Open the shopping cart via the success notification popup.
        shopping_cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        shopping_cart_link.click()

        # 5. Accept terms of service and click the "Checkout" button.
        try:
            terms_of_service_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
            terms_of_service_checkbox.click()
        except NoSuchElementException:
            self.fail("Terms of service checkbox is missing.")

        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill in the billing address.
        first_name_input = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        first_name_input.send_keys(self.credentials["FirstName"])

        last_name_input = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_LastName")))
        last_name_input.send_keys(self.credentials["LastName"])

        email_input = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_Email")))
        email_input.send_keys(f"user_{self.credentials['Email']}@test.com")

        country_select = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_select.click()
        country_select.send_keys("United States of America")

        state_select = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
        state_select.click()
        state_select.send_keys("Other")

        city_input = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_City")))
        city_input.send_keys(self.credentials["City"])

        address1_input = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_Address1")))
        address1_input.send_keys(self.credentials["Address1"])

        zip_postal_code_input = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode")))
        zip_postal_code_input.send_keys(self.credentials["ZipPostalCode"])

        phone_number_input = wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_PhoneNumber")))
        phone_number_input.send_keys(self.credentials["PhoneNumber"])

        billing_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button")))
        billing_continue_button.click()

        # 8. Select shipping and payment methods.
        shipping_method_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["ShippingOption"])))
        shipping_method_option.click()

        shipping_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button")))
        shipping_continue_button.click()

        payment_method_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.credentials["PaymentMethodOption"])))
        payment_method_option.click()

        payment_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button")))
        payment_continue_button.click()

        # 9. Enter credit card details.
        cardholder_name_input = wait.until(EC.visibility_of_element_located((By.ID, "CardholderName")))
        cardholder_name_input.send_keys(self.credentials["CardholderName"])

        card_number_input = wait.until(EC.visibility_of_element_located((By.ID, "CardNumber")))
        card_number_input.send_keys(self.credentials["CardNumber"])

        expire_month_select = wait.until(EC.visibility_of_element_located((By.ID, "ExpireMonth")))
        expire_month_select.click()
        expire_month_select.send_keys(self.credentials["ExpireMonth"])

        expire_year_select = wait.until(EC.visibility_of_element_located((By.ID, "ExpireYear")))
        expire_year_select.click()
        expire_year_select.send_keys(self.credentials["ExpireYear"])

        card_code_input = wait.until(EC.visibility_of_element_located((By.ID, "CardCode")))
        card_code_input.send_keys(self.credentials["CardCode"])

        payment_info_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button")))
        payment_info_continue_button.click()

        # 10. Confirm the order.
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CLASS