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
        self.base_url = "http://max/"
        self.email = f"user_{time.strftime('%H%M%S')}_z@test.com"

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # Search for a product
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_box.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # Add the first product to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart failed: {e}")

        # Go to shopping cart
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to shopping cart: {e}")

        # Checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout failed: {e}")

        # Checkout as guest
        try:
            guest_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            guest_checkout_button.click()
        except Exception as e:
            self.fail(f"Guest checkout failed: {e}")

        # Billing address form
        try:
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            first_name_field.send_keys("Test")

            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            last_name_field.send_keys("User")

            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            email_field.send_keys(self.email)

            country_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            country_dropdown.send_keys("Latvia")

            state_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
            )
            state_dropdown.send_keys("Other")

            city_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            city_field.send_keys("Riga")

            address1_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            address1_field.send_keys("Street 1")

            zip_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            zip_field.send_keys("LV-1234")

            phone_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )
            phone_field.send_keys("12345678")

            billing_continue_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "new-address-next-step-button"))
            )
            billing_continue_button.click()

        except Exception as e:
            self.fail(f"Billing address form failed: {e}")

        # Shipping method
        try:
            shipping_method_option = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "shippingoption_1"))
            )
            shipping_method_option.click()

            shipping_continue_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_continue_button.click()
        except Exception as e:
            self.fail(f"Shipping method selection failed: {e}")

        # Payment method
        try:
            payment_method_option = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "paymentmethod_1"))
            )
            payment_method_option.click()

            payment_continue_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            payment_continue_button.click()
        except Exception as e:
            self.fail(f"Payment method selection failed: {e}")

        # Payment information
        try:
            card_type_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CreditCardType"))
            )
            card_type_dropdown.send_keys("visa")

            cardholder_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardholderName"))
            )
            cardholder_name_field.send_keys("Test User")

            card_number_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardNumber"))
            )
            card_number_field.send_keys("4111111111111111")

            expire_month_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ExpireMonth"))
            )
            expire_month_dropdown.send_keys("4")

            expire_year_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ExpireYear"))
            )
            expire_year_dropdown.send_keys("2027")

            card_code_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardCode"))
            )
            card_code_field.send_keys("123")

            payment_info_continue_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "payment-info-next-step-button"))
            )
            payment_info_continue_button.click()