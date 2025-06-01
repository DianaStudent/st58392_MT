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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
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
            self.fail(f"Going to shopping cart failed: {e}")

        # Agree to terms of service and checkout
        try:
            terms_of_service_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "termsofservice"))
            )
            terms_of_service_checkbox.click()
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
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            first_name_input.send_keys("Test")
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            last_name_input.send_keys("User")
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            email_input.send_keys("random_email")
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            for option in country_select.find_elements(By.TAG_NAME, 'option'):
                if option.get_attribute('value') == '124':
                    option.click()
                    break
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
            )
            for option in state_select.find_elements(By.TAG_NAME, 'option'):
                if option.get_attribute('value') == '0':
                    option.click()
                    break
            city_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            city_input.send_keys("Riga")
            address1_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            address1_input.send_keys("Street 1")
            zip_postal_code_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            zip_postal_code_input.send_keys("LV-1234")
            phone_number_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )
            phone_number_input.send_keys("12345678")
            billing_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            billing_continue_button.click()
        except Exception as e:
            self.fail(f"Billing form failed: {e}")

        # Shipping method
        try:
            shipping_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "shippingoption_1"))
            )
            shipping_option.click()
            shipping_method_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_method_continue_button.click()
        except Exception as e:
            self.fail(f"Shipping method failed: {e}")

        # Payment method
        try:
            payment_method_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "paymentmethod_1"))
            )
            payment_method_option.click()
            payment_method_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            payment_method_continue_button.click()
        except Exception as e:
            self.fail(f"Payment method failed: {e}")

         # Payment information
        try:
            credit_card_type_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CreditCardType"))
            )
            for option in credit_card_type_select.find_elements(By.TAG_NAME, 'option'):
                if option.get_attribute('value') == 'visa':
                    option.click()
                    break
            cardholder_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardholderName"))
            )
            cardholder_name_input.send_keys("Test User")
            card_number_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardNumber"))
            )
            card_number_input.send_keys("4111111111111111")
            expire_month_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ExpireMonth"))
            )
            for option in expire_month_select.find_elements(By.TAG_NAME, 'option'):
                if option.get_attribute('value') == '4':
                    option.click()
                    break
            expire_year_