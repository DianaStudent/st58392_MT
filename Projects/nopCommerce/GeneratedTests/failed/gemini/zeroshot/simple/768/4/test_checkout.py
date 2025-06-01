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
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_input.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # Add the first product to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding to cart failed: {e}")

        # Go to shopping cart
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Navigating to shopping cart failed: {e}")

        # Agree to terms of service
        try:
            terms_of_service_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "termsofservice"))
            )
            terms_of_service_checkbox.click()
        except Exception as e:
            self.fail(f"Terms of service agreement failed: {e}")

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
            country_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
            country_dropdown.send_keys(Keys.ARROW_DOWN)
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
            shipping_method_option = WebDriverWait(driver, 20).