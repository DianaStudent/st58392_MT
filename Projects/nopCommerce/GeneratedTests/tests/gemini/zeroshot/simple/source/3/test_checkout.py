```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        # Search for a product
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # Add the first product to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding to cart failed: {e}")

        # Go to the shopping cart
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[contains(@href, '/cart')]"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Navigating to shopping cart failed: {e}")

        # Checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout failed: {e}")

        # Checkout as guest
        try:
            checkout_as_guest_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            checkout_as_guest_button.click()
        except Exception as e:
            self.fail(f"Checkout as guest failed: {e}")

        # Billing form
        try:
            first_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            first_name.send_keys("Test")
            last_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            last_name.send_keys("User")
            email = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            email.send_keys("random_email")
            country = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            country.send_keys("Latvia")
            city = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            city.send_keys("Riga")
            address1 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            address1.send_keys("Street 1")
            zip_postal_code = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            zip_postal_code.send_keys("LV-1234")
            phone_number = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )
            phone_number.send_keys("12345678")

            continue_button_billing = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            continue_button_billing.click()

        except Exception as e:
            self.fail(f"Billing form failed: {e}")
        
        # Shipping method
        try:
            shipping_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "shippingoption_1"))
            )
            shipping_option.click()
            continue_button_shipping = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            continue_button_shipping.click()
        except Exception as e:
            self.fail(f"Shipping method failed: {e}")

        # Payment method
        try:
            payment_method_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "paymentmethod_1"))
            )
            payment_method_option.click()
            continue_button_payment = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            continue_button_payment.click()
        except Exception as e:
            self.fail(f"Payment method failed: {e}")

        # Payment information
        try:
            cardholder_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardholderName"))
            )
            cardholder_name.send_keys("Test User")
            card_number = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardNumber"))
            )
            card_number.send_keys("4111111111111111")
            expire_month = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ExpireMonth"))
            )
            expire_month.send_keys("4")
            expire_year = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ExpireYear"))
            )
            expire_year.send_keys("2027")
            card_code = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardCode"))
            )
            card_code.send_keys("123")

            continue_button_payment_info = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button"))
            )
            continue_button_payment_info.click()
        except Exception as e:
            self.fail(f"Payment information failed: {e}")

        # Confirm order
        try:
            confirm_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
            )
            confirm_button.click()
        except Exception as e:
            self.fail(f"Confirm order failed: {e}")

        # Verify order completion
        try:
            order_completed_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='title']/strong[contains(text(), 'Your order has been successfully processed!')]"))
            )
            self.assertIn("Your order has been successfully processed!", order_completed_message.text)
        except Exception