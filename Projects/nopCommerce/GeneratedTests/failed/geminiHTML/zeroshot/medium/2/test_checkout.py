from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Search" link and search for a product (e.g. "book").
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_input.send_keys("book")

        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-button")))
        search_button.click()

        # 3. Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. Open the shopping cart via the success notification popup.
        shopping_cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        shopping_cart_link.click()

        # 5. Accept terms of service and click the "Checkout" button.
        try:
            terms_of_service_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
            terms_of_service_checkbox.click()
        except:
            self.fail("Terms of service checkbox not found")

        try:
            checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
            checkout_button.click()
        except:
            self.fail("Checkout button not found")

        # 6. Choose "Checkout as Guest".
        try:
            checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
            checkout_as_guest_button.click()
        except:
            self.fail("Checkout as guest button not found")

        # 7. Fill in the billing address.
        try:
            first_name_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName")))
            first_name_input.send_keys("Test")
        except:
            self.fail("First name input not found")

        try:
            last_name_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_LastName")))
            last_name_input.send_keys("User")
        except:
            self.fail("Last name input not found")

        try:
            email_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_Email")))
            email_input.send_keys("random_email@test.com")
        except:
            self.fail("Email input not found")

        try:
            country_select = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
            country_select.send_keys("Latvia")
        except:
            self.fail("Country select not found")

        try:
            state_select = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
            state_select.send_keys("Other")
        except:
            self.fail("State select not found")

        try:
            city_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_City")))
            city_input.send_keys("Riga")
        except:
            self.fail("City input not found")

        try:
            address1_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_Address1")))
            address1_input.send_keys("Street 1")
        except:
            self.fail("Address1 input not found")

        try:
            zip_postal_code_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_ZipPostalCode")))
            zip_postal_code_input.send_keys("LV-1234")
        except:
            self.fail("ZipPostalCode input not found")

        try:
            phone_number_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_PhoneNumber")))
            phone_number_input.send_keys("12345678")
        except:
            self.fail("PhoneNumber input not found")

        try:
            billing_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button")))
            billing_continue_button.click()
        except:
            self.fail("Billing continue button not found")

        # 8. Select shipping and payment methods.
        try:
            shipping_method_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
            shipping_method_option.click()
        except:
            self.fail("Shipping option not found")

        try:
            shipping_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button")))
            shipping_continue_button.click()
        except:
            self.fail("Shipping continue button not found")

        try:
            payment_method_option = wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
            payment_method_option.click()
        except:
            self.fail("Payment method option not found")

        try:
            payment_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button")))
            payment_continue_button.click()
        except:
            self.fail("Payment continue button not found")

        # 9. Enter credit card details.
        try:
            cardholder_name_input = wait.until(EC.element_to_be_clickable((By.ID, "CardholderName")))
            cardholder_name_input.send_keys("Test User")
        except:
            self.fail("Cardholder name input not found")

        try:
            card_number_input = wait.until(EC.element_to_be_clickable((By.ID, "CardNumber")))
            card_number_input.send_keys("4111111111111111")
        except:
            self.fail("Card number input not found")

        try:
            expire_month_select = wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth")))
            expire_month_select.send_keys("4")
        except:
            self.fail("Expire month select not found")

        try:
            expire_year_select = wait.until(EC.presence_of_element_located((By.ID, "ExpireYear")))
            expire_year_select.send_keys("2027")
        except:
            self.fail("Expire year select not found")

        try:
            card_code_input = wait.until(EC.element_to_be_clickable((By.ID, "CardCode")))
            card_code_input.send_keys("123")
        except:
            self.fail("Card code input not found")

        try:
            payment_info_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_