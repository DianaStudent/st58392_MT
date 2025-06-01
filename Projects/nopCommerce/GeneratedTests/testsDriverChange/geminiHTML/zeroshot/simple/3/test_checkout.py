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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
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
            self.fail(f"Adding to cart failed: {e}")

        # Go to the shopping cart
        try:
            shopping_cart_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='bar-notification success']//a[contains(@href, '/cart')]"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Navigating to shopping cart failed: {e}")

        # Agree with terms of service
        try:
            terms_of_service_checkbox = wait.until(
                EC.element_to_be_clickable((By.ID, "termsofservice"))
            )
            terms_of_service_checkbox.click()
        except Exception as e:
            self.fail(f"Terms of service agreement failed: {e}")

        # Click Checkout
        try:
            checkout_button = wait.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout failed: {e}")

        # Checkout as Guest
        try:
            guest_checkout_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            guest_checkout_button.click()
        except Exception as e:
            self.fail(f"Guest checkout failed: {e}")

        # Fill in billing form
        try:
            first_name = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            first_name.send_keys("Test")

            last_name = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            last_name.send_keys("User")

            email = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            email.send_keys("random_email@test.com")

            country = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            country.send_keys("Latvia")

            state = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
            state.send_keys("Other")

            city = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            city.send_keys("Riga")

            address1 = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            address1.send_keys("Street 1")

            zip_code = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            zip_code.send_keys("LV-1234")

            phone_number = wait.until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )
            phone_number.send_keys("12345678")

            billing_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            billing_continue_button.click()

        except Exception as e:
            self.fail(f"Billing form failed: {e}")

        # Shipping Method
        try:
            shipping_method = wait.until(
                EC.element_to_be_clickable((By.ID, "shippingoption_1"))
            )
            shipping_method.click()

            shipping_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_continue_button.click()
        except Exception as e:
            self.fail(f"Shipping method failed: {e}")

        # Payment Method
        try:
            payment_method = wait.until(
                EC.element_to_be_clickable((By.ID, "paymentmethod_1"))
            )
            payment_method.click()

            payment_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            payment_continue_button.click()
        except Exception as e:
            self.fail(f"Payment method failed: {e}")

        # Payment Info
        try:
            card_type = wait.until(
                EC.presence_of_element_located((By.ID, "CreditCardType"))
            )
            card_type.send_keys("visa")

            cardholder_name = wait.until(
                EC.presence_of_element_located((By.ID, "CardholderName"))
            )
            cardholder_name.send_keys("Test User")

            card_number = wait.until(
                EC.presence_of_element_located((By.ID, "CardNumber"))
            )
            card_number.send_keys("4111111111111111")

            expire_month = wait.until(
                EC.presence_of_element_located((By.ID, "ExpireMonth"))
            )
            expire_month.send_keys("4")

            expire_year = wait.until(
                EC.presence_of_element_located((By.ID, "ExpireYear"))
            )
            expire_year.send_keys("2027")

            card_code = wait.until(
                EC.presence_of_element_located((By.ID, "CardCode"))
            )
            card_code.send_keys("123")

            payment_info_continue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button"))
            )
            payment_info_continue_button.click()
        except Exception as e:
            self.fail(f"Payment info failed: {e}")

        # Confirm Order
        try:
            confirm_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
            )
            confirm_button.click()
        except Exception as e:
            self.fail(f"Confirm order failed: {e}")

        # Verify order completion
        try:
            order_completed_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='title']/strong[contains(text(), 'Your order has been successfully processed!')]"))
            )
            self.assertTrue(order_completed