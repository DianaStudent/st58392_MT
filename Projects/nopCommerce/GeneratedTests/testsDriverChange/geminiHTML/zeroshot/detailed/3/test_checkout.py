```python
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        self.base_url = "http://max/"
        self.credentials = {
            "FirstName": "Test",
            "LastName": "User",
            "City": "Riga",
            "Address1": "Street 1",
            "ZipPostalCode": "LV-1234",
            "PhoneNumber": "12345678",
            "CountryId": "237", # United States of America
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
        self.random_email = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + "@test.com"

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # 2. Navigate to the "Search" page and look for a product using the query "book".
        try:
            search_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click the 'Search' link: {e}")

        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
            search_input.send_keys("book")
            search_button.click()
        except Exception as e:
            self.fail(f"Failed to find or interact with the search input/button: {e}")

        # 3. Add the first result to the cart using a product tile button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click the 'Add to cart' button: {e}")

        # 4. From the success notification, click the "shopping cart" link.
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='bar-notification success']//a[text()='shopping cart']"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Failed to find or click the 'shopping cart' link in the notification: {e}")

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        try:
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "termsofservice"))
            )
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout"))
            )
            terms_checkbox.click()
            checkout_button.click()
        except Exception as e:
            self.fail(f"Failed to find or interact with the 'Terms of service' checkbox or 'Checkout' button: {e}")

        # 6. Choose "Checkout as Guest".
        try:
            checkout_as_guest_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            checkout_as_guest_button.click()
        except Exception as e:
            self.fail(f"Failed to find or click the 'Checkout as Guest' button: {e}")

        # 7. Fill out the full billing form (from credentials).
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys(self.credentials["FirstName"])
            driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys(self.credentials["LastName"])
            driver.find_element(By.ID, "BillingNewAddress_Email").send_keys(self.random_email)
            driver.find_element(By.ID, "BillingNewAddress_City").send_keys(self.credentials["City"])
            driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys(self.credentials["Address1"])
            driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys(self.credentials["ZipPostalCode"])
            driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys(self.credentials["PhoneNumber"])

            country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
            country_select.click()
            country_select.send_keys("United States of America")

            state_select = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
            state_select.click()
            state_select.send_keys("Other")

            continue_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "new-address-next-step-button"))
            )
            continue_button.click()

        except Exception as e:
            self.fail(f"Failed to fill out the billing form: {e}")

        # 8. Proceed through the following steps:
        # - Shipping method step.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout-step-shipping-method"))
            )
            shipping_option = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.credentials["ShippingOption"]))
            )
            shipping_option.click()

            shipping_method_continue_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_method_continue_button.click()
        except Exception as e:
            self.fail(f"Failed to select shipping method and continue: {e}")

        # - Payment method step.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "checkout-step-payment-method"))
            )
            payment_method_option = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#paymentmethod_1"))
            )
            payment_method_option.click()

            payment_method_continue_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            payment_method_continue_button.click()
        except Exception as e:
            self.fail