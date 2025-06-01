from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.url = "http://max/"
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product
        try:
            search_input = wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_input.send_keys("book")
            search_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # Add the first product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart failed: {e}")

        # Go to the shopping cart
        try:
            shopping_cart_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to shopping cart: {e}")

        # Agree to terms of service and checkout
        try:
            terms_of_service_checkbox = wait.until(
                EC.element_to_be_clickable((By.ID, "termsofservice"))
            )
            terms_of_service_checkbox.click()

            checkout_button = wait.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout failed: {e}")

        # Checkout as guest
        try:
            checkout_as_guest_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            checkout_as_guest_button.click()
        except Exception as e:
            self.fail(f"Checkout as guest failed: {e}")

        # Fill in billing information
        try:
            first_name_input = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            first_name_input.send_keys("Test")

            last_name_input = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            last_name_input.send_keys("User")

            email_input = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            email_input.send_keys("random_email")

            country_select = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            country_select.send_keys("Latvia")

            city_input = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            city_input.send_keys("Riga")

            address1_input = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            address1_input.send_keys("Street 1")

            zip_postal_code_input = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            zip_postal_code_input.send_keys("LV-1234")

            phone_number_input = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )
            phone_number_input.send_keys("12345678")

            continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            continue_button.click()
        except Exception as e:
            self.fail(f"Billing information failed: {e}")

        # Select shipping method
        try:
            shipping_option = wait.until(
                EC.element_to_be_clickable((By.ID, "shippingoption_1"))
            )
            shipping_option.click()

            shipping_method_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_method_continue_button.click()
        except Exception as e:
            self.fail(f"Shipping method selection failed: {e}")

        # Select payment method
        try:
            payment_method_option = wait.until(
                EC.element_to_be_clickable((By.ID, "paymentmethod_1"))
            )
            payment_method_option.click()

            payment_method_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            payment_method_continue_button.click()
        except Exception as e:
            self.fail(f"Payment method selection failed: {e}")

        # Fill in payment information
        try:
            credit_card_type_select = wait.until(
                EC.presence_of_element_located((By.ID, "CreditCardType"))
            )
            credit_card_type_select.send_keys("visa")

            cardholder_name_input = wait.until(
                EC.presence_of_element_located((By.ID, "CardholderName"))
            )
            cardholder_name_input.send_keys("Test User")

            card_number_input = wait.until(
                EC.presence_of_element_located((By.ID, "CardNumber"))
            )
            card_number_input.send_keys("4111111111111111")

            expire_month_select = wait.until(
                EC.presence_of_element_located((By.ID, "ExpireMonth"))
            )
            expire_month_select.send_keys("4")

            expire_year_select = wait.until(
                EC.presence_of_element_located((By.ID, "ExpireYear"))
            )
            expire_year_select.send_keys("2027")

            card_code_input = wait.until(
                EC.presence_of_element_located((By.ID, "CardCode"))
            )
            card_code_input.send_keys("123")

            payment_info_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button"))
            )
            payment_info_continue_button.click()
        except Exception as e:
            self.fail(f"Payment information failed: {e}")

        # Confirm order
        try:
            confirm_order_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
            )
            confirm_order_button.click()
        except Exception as e:
            self.fail(f"Confirm order failed: {e}")

        # Verify order completion
        try:
            order_completed_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@